from views.header_window import *
from views.disk_window import *
from controllers.disk_controller import DiskController
from controllers.header_controller import HeaderController
from models.disk_model import DiskModel
from models.header_model import HeaderModel
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from PyQt5.QtGui import QPalette, QColor

__version__ = "0.0.1"

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle(f"FDC-SDS-GUI v{__version__}")                           

        v_layout = QVBoxLayout()        
        v_layout.addWidget(self.create_header_window())        

        v_layout.addWidget(self.create_disk_window(0))
        v_layout.addWidget(self.create_disk_window(1))
        v_layout.addWidget(self.create_disk_window(2))
        v_layout.addWidget(self.create_disk_window(3))

        self.setFixedSize(QSize(500,600))
        widget = QWidget()
        widget.setLayout(v_layout)
        self.setCentralWidget(widget)

    def create_header_window(self):
        header_window = HeaderWindow(None)
        header_model = HeaderModel()
        header_window.set_controller(HeaderController(header_window, header_model))
        return header_window

    def create_disk_window(self, number):
        disk_window = DiskWindow(number, None)
        disk_model = DiskModel(number)
        disk_window.set_controller(DiskController(disk_window, disk_model))
        return disk_window
    
        
