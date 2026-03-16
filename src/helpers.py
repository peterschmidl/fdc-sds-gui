import serial.tools.list_ports

class Helpers:
    def get_serial_ports():
        ports = serial.tools.list_ports.comports()
        return [port.device for port in ports]