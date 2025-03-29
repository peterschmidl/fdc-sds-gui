class DiskController:
    def __init__(self, view, model):
        self.view = view
        self.model = model

    def handle_load_click(self):
        path = self.model.load_disk()
        self.view.set_path_text(path)

    def handle_unload_click(self):
        path = self.model.unload_disk()
        self.view.set_path_text(path)
