class HeaderController:
    def __init__(self, view, model, log, on_change=None):
        self.view = view
        self.model = model
        self.log = log
        self.on_change = on_change
        self.view.populate_com_ports(self.model.get_com_ports())
        self.view.populate_baud_rates(self.model.get_baud_rates())
        self.set_default_baud_rate()
        self.set_default_com_port()

    def set_default_com_port(self):
        for index, com_port in enumerate(self.model.get_com_ports()):
            if com_port == self.model.get_current_com_port():
                self.view.set_current_com_port(index)
                break

    def set_default_baud_rate(self):
        for index, baudrate in enumerate(self.model.get_baud_rates()):
            if baudrate == self.model.get_current_baud_rate():
                self.view.set_current_baud_rate(index)
                break

    def handle_com_port_change(self):
        com_port = self.view.ports.currentText()
        self.model.set_current_com_port(com_port)
        self.log.log(f"Port selected: {com_port}")
        if self.on_change:
            self.on_change()

    def handle_baudrate_change(self):
        baud_rate = self.view.baud_rates.currentText()
        self.model.set_current_baud_rate(baud_rate)
        self.log.log(f"Baud rate selected: {baud_rate}")
        if self.on_change:
            self.on_change()
