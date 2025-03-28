from views.header_window import *
from views.disk_window import *
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from PyQt5.QtGui import QPalette, QColor

__version__ = "0.0.1"

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle(f"FDC-SDS-GUI v{__version__}")                           

        v_layout = QVBoxLayout()
        v_layout.addWidget(HeaderWindow(self))
        v_layout.addWidget(DiskWindow(self))

        self.setFixedSize(QSize(500,600))
        widget = QWidget()
        widget.setLayout(v_layout)

        self.setCentralWidget(widget)
    
        
