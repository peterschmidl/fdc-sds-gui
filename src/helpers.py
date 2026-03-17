import sys
import serial.tools.list_ports
from PyQt5.QtWidgets import QMessageBox

class Helpers:
    def get_serial_ports():
        ports = serial.tools.list_ports.comports()
        return [
            port.name for port in ports
            if port.serial_number is not None
            and (sys.platform != 'darwin' or '/cu.' in port.device)
        ]

    def show_message(message, icon, window_title):
        msg = QMessageBox()
        msg.setIcon(icon)
        msg.setWindowTitle(window_title)
        msg.setText(message)
        msg.exec()    