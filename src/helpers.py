import sys
import serial.tools.list_ports

class Helpers:
    def get_serial_ports():
        ports = serial.tools.list_ports.comports()
        return [
            port.device for port in ports
            if port.serial_number is not None
            and (sys.platform != 'darwin' or '/cu.' in port.device)
        ]