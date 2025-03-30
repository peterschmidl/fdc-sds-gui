from helpers import *

class HeaderModel:
    def __init__(self):
        self.com_ports = Helpers.get_serial_ports()
        self.current_com_port = self.com_ports[0]
        
        self.baudrates = ["403.2K", "460.8K", "230.4K", "76.8K", "57.6K", "38.4K", "19.2K", "9.6K"]
        self.current_baudrate = self.baudrates[0]
        
        self.connected = False

    def set_current_baud_rate(self, value):
        self.current_baudrate = value

    def get_current_baud_rate(self):
        return self.current_baudrate
    
    def get_baud_rates(self):
        return self.baudrates

    def set_current_com_port(self, value):
        self.current_com_port = value

    def get_current_com_port(self):
        return self.current_com_port
    
    def get_com_ports(self):
        return self.com_ports

