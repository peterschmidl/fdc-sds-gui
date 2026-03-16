import sys
import shutil
from views.main_window import *
from PyQt5.QtWidgets import QApplication, QMessageBox

app = QApplication(sys.argv)

if shutil.which("fdcsds") is None:
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setWindowTitle("FDC-SDS-GUI Error")
    msg.setText('<b>fdcsds</b> command not found in PATH.<br>Please install <a href="https://github.com/deltecent/fdc-sds">FDC-SDS Serial Disk Server</a> before running this application.')
    msg.exec()
    sys.exit(1)

window = MainWindow()
window.show()

# Start the event loop.
app.exec()