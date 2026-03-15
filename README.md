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

### macOS
macOS may block the binary because it is not signed. To fix this, run:
```bash
xattr -d com.apple.quarantine fdc-sds-gui-macos
chmod +x fdc-sds-gui-macos
./fdc-sds-gui-macos
```
