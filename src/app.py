import sys
import shutil
from views.main_window import *
from PyQt5.QtWidgets import QApplication

app = QApplication(sys.argv)

if not sys.platform.startswith('darwin') and not sys.platform.startswith('linux'):
    Helpers.show_message('Unsupported platform (Linux and MacOS are supported)', QMessageBox.Critical, 'FDC-SDS-GUI Error')
    sys.exit(1)

if shutil.which("fdcsds") is None:
    Helpers.show_message('<b>fdcsds</b> command not found in PATH.<br>Please install <a href="https://github.com/deltecent/fdc-sds">FDC-SDS Serial Disk Server</a> before running this application.',
                         QMessageBox.Critical, 'FDC-SDS-GUI Error')        
    sys.exit(1)

window = MainWindow()
window.show()

# Start the event loop.
app.exec()