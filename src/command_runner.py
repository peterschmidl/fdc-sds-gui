import subprocess
from shutil import which


class CommandRunner:
    def __init__(self):
        self.sds_command = "fdcsds"
        self._process = None

    def run(self, port, baud, disk_paths, log):
        self._stop()
        if not disk_paths:
            return False
        if not self.check_fdcsds_present():
            log.log(f"Error: '{self.sds_command}' not found in PATH")
            return False
        args = [self.sds_command, "-p", f"/dev/{port}", "-b", str(baud)]
        for i in sorted(disk_paths):
            args += [f"-{i}", disk_paths[i]]
        log.log(f"Running: {' '.join(args)}")
        try:
            self._process = subprocess.Popen(args)
            return True
        except Exception as e:
            log.log(f"Failed to start fdcsds: {e}")
            return False

    def _stop(self):
        if self._process and self._process.poll() is None:
            self._process.terminate()
            self._process = None

    def stop(self):
        self._stop()
        return False

    def check_fdcsds_present(self):
        return which(self.sds_command) is not None
