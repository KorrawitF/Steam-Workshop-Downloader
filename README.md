# Steam Workshop Downloader

Tools for bulk-downloading Arma 3 Steam Workshop mods through SteamCMD and renaming the numeric workshop folders into readable `@ModName` directories the game can load.

Downloading a mod with SteamCMD leaves it in a folder named after its workshop ID. These scripts scrape each mod's real title from its Workshop page and rename the folder accordingly, so a whole modlist can be fetched in one pass.

## What's in here

| File | Description |
| --- | --- |
| `ModLoader 3.0.py` | Tkinter GUI version — pick the SteamCMD and output directories, paste a comma-separated list of Workshop URLs, watch a progress bar |
| `ModLoader 2.0.py` | Console version — prompts for comma-separated Workshop URLs and downloads them in order |
| `Modloader.bat` | Standalone Windows batch downloader with a hard-coded modlist (~30 Arma 3 mods) and per-mod on/off flags |
| `namechanger.py` | Standalone repair script: renames already-downloaded workshop-ID folders using a JSON ID → name map |

## How the Python versions work

1. URLs are pushed onto a small `Queue` class and processed recursively one at a time.
2. The mod ID is split off the URL (`...?id=<ID>`).
3. `requests` + **BeautifulSoup** fetch the Workshop page and read `workshopItemTitle` for the mod's real name.
4. **pysteamcmdwrapper** installs SteamCMD if needed, logs in anonymously, and calls `workshop_update` for Arma 3 (app ID `107410`).
5. The downloaded folder is renamed from the ID to `@Mod-Name`, with punctuation stripped; any existing folder with that name is removed first.

## Requirements

```bash
pip install pysteamcmdwrapper beautifulsoup4 requests
```

Windows, plus Tkinter for version 3.0 (bundled with standard Python installs).

## Usage

**GUI:**
```bash
python "ModLoader 3.0.py"
```
Choose the SteamCMD directory and the mod output directory, paste Workshop links separated by commas, then press *Start*.

**Console:**
```bash
python "ModLoader 2.0.py"
# Enter links here seperate by comma e.g(Link1, Link2):
```

**Batch:** edit the `ModName[n]` / `Mod[n]` / `ModDownload[n]` entries at the top of `Modloader.bat`, then run it.

## Notes

- Hard-wired to Arma 3 (app ID `107410`); change that ID to target another game.
- `namechanger.py` contains an absolute path and an inline JSON map from a specific modlist — edit both before reusing it.
- Anonymous SteamCMD login only works for mods that do not require an owning account.
