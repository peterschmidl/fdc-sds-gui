# fdc-sds-gui
GUI for [FDC-SDS Serial Disk Server](https://github.com/deltecent/fdc-sds) for the Altair FDC+
on Linux and MacOS

## Installation

Download the latest binary for your platform from the [Releases](https://github.com/peterschmidl/fdc-sds-gui/releases) page.

### Linux
```bash
chmod +x fdc-sds-gui-linux
./fdc-sds-gui-linux
```

### macOS (Apple Silicon)
macOS may block the binary because it is not signed. To fix this, run:
```bash
xattr -d com.apple.quarantine fdc-sds-gui-macos
chmod +x fdc-sds-gui-macos
./fdc-sds-gui-macos
```

### macOS (Intel)
No native Intel binary is provided. The Apple Silicon binary runs on Intel Macs via **Rosetta 2**.
If Rosetta 2 is not yet installed, macOS will prompt you to install it automatically on first run, or you can install it manually:
```bash
softwareupdate --install-rosetta
```
Then follow the same steps as for Apple Silicon above.
