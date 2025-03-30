class DiskModel:
    def __init__(self, disk_number):
        self.disk_number = disk_number
        self.path = ""
        self.status = "Idle"

    def set_path(self, path):        
        self.path = path
        self.status = "Loaded"

    def get_path(self):
        return self.path
