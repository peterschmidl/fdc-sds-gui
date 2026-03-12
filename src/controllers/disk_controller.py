class DiskController:
    def __init__(self, view, model, log, on_change):
        self.view = view
        self.model = model
        self.log = log
        self.on_change = on_change

    def handle_load_click(self):
        path = self.view.get_path()
        if path:
            self.model.set_path(path)
            self.view.set_path(self.model.get_path())
            self.log.log(f"Disk {self.model.disk_number} loaded: {path}")
            self.on_change()

    def handle_unload_click(self):
        self.model.set_path("")
        self.view.set_path(self.model.get_path())
        self.log.log(f"Disk {self.model.disk_number} unloaded")
        self.on_change()
