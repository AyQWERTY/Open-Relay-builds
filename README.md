<div align="center">

<img src="https://raw.githubusercontent.com/Ichigo3766/Open-Relay/refs/heads/main/openrelayicon.png" width="120" alt="Open Relay App Icon" style="border-radius: 22px;" />

# Open Relay

**The best native iOS/iPadOS & Watch client for [Open WebUI](https://openwebui.com)**

_Chat with any AI model on your self-hosted server — beautifully._

[![Download on the App Store](https://developer.apple.com/assets/elements/badges/download-on-the-app-store.svg)](https://apps.apple.com/app/id6759630325)

</div>

---

## What this repo is

Open Relay is written by [Ichigo3766](https://github.com/Ichigo3766/Open-Relay). This repo builds his source into an IPA you can sideload.

## Differences from upstream

- The app icon: `Contents.json` lists `or.png`, the file on disk is `OR.png`, so the home screen shows no icon. Fixed.
- Everything else is the original code, unchanged.

## Releases

Open [Releases](https://github.com/AyQWERTY/Open-Relay-builds/releases). Each release is named after the upstream version and holds one file, `Open-Relay-vX.Y.Z.ipa`, built without a signature. Sign it with your own certificate before installing.

New upstream tags are checked once a day and built automatically, so the newest version is the latest release.

## Which Xcode can build it

This took two days to work out. The build is picky about the compiler.

| Xcode                    | What happens                                                                                                                                                                              |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 26.3 and older           | Package dependencies fail to resolve. No build.                                                                                                                                           |
| 26.4 - 26.6              | Swift runs out of type-checking budget: "the compiler is unable to type-check this expression in reasonable time". Removing the Watch app only moves the error to another file. No build. |
| 27.1                     | Builds. This is what the workflow uses.                                                                                                                                                   |
| 27.2 (release candidate) | Builds, but the IPA crashes right after sign-in.                                                                                                                                          |
