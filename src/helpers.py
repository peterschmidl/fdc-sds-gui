import sys
import serial.tools.list_ports
import wx


class Helpers:
    def get_serial_ports():
        ports = serial.tools.list_ports.comports()
        return [
            port.name for port in ports
            if port.serial_number is not None
            and (sys.platform != 'darwin' or '/cu.' in port.device)
        ]

    def show_message(message, icon, window_title):
        wx.MessageBox(message, window_title, icon)
