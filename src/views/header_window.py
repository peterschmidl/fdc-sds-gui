from helpers import *
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QComboBox
from QLed import QLed

class HeaderWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        layout = QHBoxLayout()        
        self.ports_label = QLabel("Serial Port")
        self.ports = QComboBox()

        self.baud_rates_label = QLabel("Baud Rate")
        self.baud_rates = QComboBox()

        self.connected = QLed(self, onColour=QLed.Green, shape=QLed.Circle)

        layout.addWidget(self.ports_label)
        layout.addWidget(self.ports)
        layout.addWidget(self.baud_rates_label)
        layout.addWidget(self.baud_rates)
        layout.addWidget(self.connected)
        self.setLayout(layout) 

    def populate_baud_rates(self, baud_rates):
        self.baud_rates.clear()
        self.baud_rates.addItems(baud_rates)

    def populate_com_ports(self, com_ports):
        self.ports.clear()
        self.ports.addItems(com_ports)

    def set_current_baud_rate(self, index):
        self.baud_rates.setCurrentIndex(index)

    def set_current_com_port(self, index):
        self.ports.setCurrentIndex(index)

    def set_controller(self, controller):
        self.controller = controller
        self.ports.currentIndexChanged.connect(self.controller.handle_com_port_change)
        self.baud_rates.currentIndexChanged.connect(self.controller.handle_baudrate_change)        