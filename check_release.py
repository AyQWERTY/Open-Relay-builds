#!/usr/bin/env python3
"""Print up to MAX_BUILDS newest upstream Open Relay tags that this repo has no release for.

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


def main():
    tags = [tag["name"] for tag in api(f"/repos/{UPSTREAM}/tags?per_page=100")]
    released = {
        r["tag_name"] for r in api(f"/repos/{BUILD_REPO}/releases?per_page=100")
    }

    for tag in [tag for tag in tags if tag not in released][:MAX_BUILDS]:
        print(tag)


if __name__ == "__main__":
    main()
