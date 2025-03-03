import sys
from helpers import Helpers
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QComboBox, QCheckBox, QLabel
from PyQt5.QtGui import QPalette, QColor

__version__ = "0.0.1"

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle(f"FDC-SDS-GUI v{__version__}")                           
        
        h_layout_header = QHBoxLayout()
        self.init_header(h_layout_header)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout_header)

        self.setFixedSize(QSize(500,600))
        widget = QWidget()
        widget.setLayout(v_layout)

        self.setCentralWidget(widget)
    
    def init_header(self, header):
        ports_label = QLabel("Serial Port")
        ports = QComboBox()
        ports.addItems(Helpers.get_serial_ports())
        
        baud_rate_label = QLabel("Baud Rate")
        baud_rate = QComboBox()
        baud_rate.addItems(["403.2K", "460.8K", "230.4K", "76.8K", "57.6K", "38.4K", "19.2K", "9.6K"])

        status_label = QLabel("Serial Rcv")
        status = QCheckBox()
        status.isCheckable = False
        status.setChecked = False

        header.addWidget(ports_label)
        header.addWidget(ports)
        header.addWidget(baud_rate_label)
        header.addWidget(baud_rate)
        header.addWidget(status_label)
        header.addWidget(status)

    def init_disk(self, layout, disk_number):
        disk_label = QLabel(f"Disk {disk_number}")

app = QApplication(sys.argv)

# Create a Qt widget, which will be our window.
window = MainWindow()
window.show()

# Start the event loop.
app.exec()