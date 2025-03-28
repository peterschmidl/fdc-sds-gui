from helpers import *
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QComboBox

class HeaderWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        layout = QHBoxLayout()
        self.ports_label = QLabel("Serial Port")
        self.ports = QComboBox()
        self.ports.addItems(Helpers.get_serial_ports())

        self.baud_rates_label = QLabel("Baud Rate")
        self.baud_rates = QComboBox()
        self.baud_rates.addItems(["403.2K", "460.8K", "230.4K", "76.8K", "57.6K", "38.4K", "19.2K", "9.6K"])

        layout.addWidget(self.ports_label)
        layout.addWidget(self.ports)
        layout.addWidget(self.baud_rates_label)
        layout.addWidget(self.baud_rates)
        self.setLayout(layout)
        # Connect signals and slots
        #self.load_button.clicked.connect(self.on_load_button_click)

    def on_load_button_click(self):
        self.label.setText("Button Clicked!")