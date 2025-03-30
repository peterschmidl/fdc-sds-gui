import subprocess

class CommandRunner:
    def __init__(self):
        self.sds_command = "fdcsds"

    def execute(self, com_port, baud_rate, disk_paths):
        subprocess.run(f"{self.sds_command} -p {com_port} -b {baud_rate}") # TODO add disk path(s)
    
    def check_fdcsds_present(self):
        from shutil import which
        return which(self.sds_command) is not None
        