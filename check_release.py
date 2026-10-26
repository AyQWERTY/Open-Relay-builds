#!/usr/bin/env python3
"""Print the newest upstream Open Relay tags newer than our latest release.

Run:
    BUILD_REPO=AyQWERTY/Open-Relay-builds GITHUB_TOKEN=... python check_release.py

No output means nothing to build. Any API failure raises.
"""

import json
import os
import urllib.request

UPSTREAM = "Ichigo3766/Open-Relay"
MAX_BUILDS = 5
BUILD_REPO = os.environ["BUILD_REPO"]
GITHUB_TOKEN = os.environ["GITHUB_TOKEN"]
API = "https://api.github.com"


def api(path):
    req = urllib.request.Request(
        API + path,
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {GITHUB_TOKEN}",
            "User-Agent": "open-relay-builds-checker",
        },
    )
    with urllib.request.urlopen(req) as resp:
        return json.load(resp)


def version(tag):
    return tuple(int(p) for p in tag.lstrip("v").split("."))


def pending(tags, released):
    # anything at or below our newest release is already covered; older upstream
    # tags are not worth building
    newest = max(map(version, released), default=())
    # oldest first: GitHub's "latest" release is the most recently created one,
    # so the newest version must be built last
    return sorted((t for t in tags if version(t) > newest), key=version)[-MAX_BUILDS:]


def main():
    tags = [tag["name"] for tag in api(f"/repos/{UPSTREAM}/tags?per_page=100")]
    released = {
        r["tag_name"] for r in api(f"/repos/{BUILD_REPO}/releases?per_page=100")
    }
    for tag in pending(tags, released):
        print(tag)


if __name__ == "__main__":
    tags = ["v6.4.1", "v6.4", "v6.3.4", "v6.10", "v6.9"]
    assert pending(tags, {"v6.10"}) == []
    assert pending(tags, {"v6.4.1"}) == ["v6.9", "v6.10"]
    assert pending(tags, set()) == ["v6.3.4", "v6.4", "v6.4.1", "v6.9", "v6.10"]
    main()
