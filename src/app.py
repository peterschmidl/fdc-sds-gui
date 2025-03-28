import sys
from views.main_window import *
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QPalette, QColor


app = QApplication(sys.argv)

window = MainWindow()
window.show()

# Start the event loop.
app.exec()