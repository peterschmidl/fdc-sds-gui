class LogController:
    def __init__(self, view):
        self.view = view

    def log(self, message):
        self.view.append(message)
