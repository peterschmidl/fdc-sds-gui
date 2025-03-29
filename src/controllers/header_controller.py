class HeaderController:
    def __init__(self, view):
        self.view = view

    def handle_com_port_changed(self):        
        self.view.set_path_text("COM port changed")

    def handle_baudrate_changed(self):    
        self.view.set_path_text("Baud rate changed")
