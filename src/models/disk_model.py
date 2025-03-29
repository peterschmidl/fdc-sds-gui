class DiskModel:
    def __init__(self, disk_number):
        self.disk_number = disk_number
        self.path = ""
        self.status = "Idle"

    def load_disk(self):        
        self.path = f"/dev/sda => {self.disk_number}"
        self.status = "Loaded"
        return self.path

    def unload_disk(self):        
        self.path = ""
        self.status = "Unloaded"
        return self.path
