import sys
import shutil
import os
from pathlib import Path
from views.main_window import *
from PyQt5.QtWidgets import QApplication

app = QApplication(sys.argv)

if not sys.platform.startswith('darwin') and not sys.platform.startswith('linux'):
    Helpers.show_message('Unsupported platform (Linux and MacOS are supported)', QMessageBox.Critical, 'FDC-SDS-GUI Error')
    sys.exit(1)

# Use bundled fdcsds if running as PyInstaller binary, otherwise fall back to submodule or PATH
_submodule_binary = Path(__file__).resolve().parents[1] / "external/fdc-sds/fdcsds"

if getattr(sys, 'frozen', False):
    fdcsds_path = str(Path(sys._MEIPASS) / 'fdcsds')
    os.chmod(fdcsds_path, 0o755)
    os.environ['FDCSDS_PATH'] = fdcsds_path
elif _submodule_binary.is_file():
    os.environ['FDCSDS_PATH'] = str(_submodule_binary)
elif shutil.which("fdcsds"):
    os.environ['FDCSDS_PATH'] = shutil.which("fdcsds")
else:
    Helpers.show_message('<b>fdcsds</b> command not found in PATH.<br>Please install <a href="https://github.com/deltecent/fdc-sds">FDC-SDS Serial Disk Server</a> before running this application.',
                         QMessageBox.Critical, 'FDC-SDS-GUI Error')
    sys.exit(1)

window = MainWindow()
window.show()

# Start the event loop.
app.exec()