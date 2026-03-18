from views.header_window import *
from views.disk_window import *
from views.log_window import LogWindow
from controllers.disk_controller import DiskController
from controllers.header_controller import HeaderController
from controllers.log_controller import LogController
from models.disk_model import DiskModel
from models.header_model import HeaderModel
from command_runner import CommandRunner
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QAction, QMessageBox
from pathlib import Path
import sys

def _get_version():
    if getattr(sys, 'frozen', False):
        base = Path(sys._MEIPASS)
    else:
        base = Path(__file__).resolve().parents[2]
    return (base / "VERSION").read_text().strip()

__version__ = _get_version()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(f"FDC-SDS-GUI v{__version__}")

        self._disk_models = []
        self._header_model = None
        self._header_view = None
        self._runner = CommandRunner()

        log_window, self.log_controller = self.create_log_window()

        v_layout = QVBoxLayout()
        v_layout.addWidget(self.create_header_window())
        for i in range(4):
            v_layout.addWidget(self.create_disk_window(i))
        v_layout.addWidget(log_window)

        self._create_menu_bar()

        self.setMinimumSize(QSize(500, 800))
        widget = QWidget()
        widget.setLayout(v_layout)
        self.setCentralWidget(widget)

    def create_log_window(self):
        log_window = LogWindow()
        log_controller = LogController(log_window)
        return log_window, log_controller

    def create_header_window(self):
        self._header_view = HeaderWindow(None)
        self._header_model = HeaderModel()
        self._header_view.set_controller(
            HeaderController(self._header_view, self._header_model, self.log_controller, self._on_config_change)
        )
        return self._header_view

    def create_disk_window(self, number):
        disk_window = DiskWindow(number, None)
        disk_model = DiskModel(number)
        self._disk_models.append(disk_model)
        disk_window.set_controller(
            DiskController(disk_window, disk_model, self.log_controller, self._on_config_change)
        )
        return disk_window

    def _create_menu_bar(self):
        menu_bar = self.menuBar()
        help_menu = menu_bar.addMenu("Help")
        about_action = QAction("About", self)
        about_action.triggered.connect(self._show_about)
        help_menu.addAction(about_action)

    def _show_about(self):
        QMessageBox.about(
            self,
            "About FDC-SDS-GUI",
            f"<h3>FDC-SDS-GUI v{__version__}</h3>"
            f"<p>GUI for <a href='https://github.com/deltecent/fdc-sds'>FDC-SDS Serial Disk Server</a> for the Altair FDC+</p>"
            f"<p><b>Author:</b> Peter Schmidl<br>"
            f"<a href='mailto:peter.schmidl@proton.me'>peter.schmidl@proton.me</a></p>"
            f"<p><b>License:</b> GPL-3.0<br>"
            f"<a href='https://github.com/peterschmidl/fdc-sds-gui'>"
            f"https://github.com/peterschmidl/fdc-sds-gui</a></p>"
        )

    def _on_config_change(self):
        port = self._header_model.get_current_com_port()
        baud = self._header_model.parse_baudrate(self._header_model.get_current_baud_rate())
        disk_paths = {m.disk_number: m.get_path() for m in self._disk_models if m.get_path()}
        running = self._runner.run(port, baud, disk_paths, self.log_controller)
        self._header_view.set_connected(running)
