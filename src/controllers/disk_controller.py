

class DiskController:
    def __init__(self, view, model):
        self.view = view
        self.model = model

    def handle_load_click(self):
        path = self.view.get_path()
        self.model.set_path(path)
        self.view.set_path(self.model.get_path())

    def handle_unload_click(self):
        self.model.set_path("")
        self.view.set_path(self.model.get_path())
