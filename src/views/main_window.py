import wx
import wx.adv
from views.header_window import HeaderWindow
from views.disk_window import DiskWindow
from views.log_window import LogWindow
from controllers.disk_controller import DiskController
from controllers.header_controller import HeaderController
from controllers.log_controller import LogController
from models.disk_model import DiskModel
from models.header_model import HeaderModel
from command_runner import CommandRunner
from pathlib import Path
import sys


def _get_version():
    if getattr(sys, 'frozen', False):
        base = Path(sys._MEIPASS)
    else:
        base = Path(__file__).resolve().parents[2]
    return (base / "VERSION").read_text().strip()

__version__ = _get_version()


class MainWindow(wx.Frame):
    def __init__(self):
        super().__init__(None, title=f"FDC-SDS-GUI v{__version__}", size=(500, 800))
        self._disk_models = []
        self._header_model = None
        self._header_view = None
        self._runner = CommandRunner()

        panel = wx.Panel(self)
        v_sizer = wx.BoxSizer(wx.VERTICAL)

        log_window, self.log_controller = self._create_log_window(panel)

        v_sizer.Add(self._create_header_window(panel), 0, wx.EXPAND | wx.ALL, 5)
        for i in range(4):
            v_sizer.Add(self._create_disk_window(panel, i), 0, wx.EXPAND | wx.ALL, 5)
        v_sizer.Add(log_window, 1, wx.EXPAND | wx.ALL, 5)

        panel.SetSizer(v_sizer)
        self._create_menu_bar()

    def _create_log_window(self, parent):
        log_window = LogWindow(parent)
        log_controller = LogController(log_window)
        return log_window, log_controller

    def _create_header_window(self, parent):
        self._header_view = HeaderWindow(parent)
        self._header_model = HeaderModel()
        self._header_view.set_controller(
            HeaderController(self._header_view, self._header_model, self.log_controller, self._on_config_change)
        )
        return self._header_view

    def _create_disk_window(self, parent, number):
        disk_window = DiskWindow(parent, number)
        disk_model = DiskModel(number)
        self._disk_models.append(disk_model)
        disk_window.set_controller(
            DiskController(disk_window, disk_model, self.log_controller, self._on_config_change)
        )
        return disk_window

    def _create_menu_bar(self):
        menu_bar = wx.MenuBar()
        help_menu = wx.Menu()
        about_item = help_menu.Append(wx.ID_ABOUT, "About")
        self.Bind(wx.EVT_MENU, self._show_about, about_item)
        menu_bar.Append(help_menu, "Help")
        self.SetMenuBar(menu_bar)

    def _show_about(self, event):
        info = wx.adv.AboutDialogInfo()
        info.SetName("FDC-SDS-GUI")
        info.SetVersion(__version__)
        info.SetDescription("GUI for FDC-SDS Serial Disk Server for the Altair FDC+")
        info.SetCopyright("(C) 2026 Peter Schmidl")
        info.AddDeveloper("Peter Schmidl <peter.schmidl@proton.me>")
        info.SetWebSite("https://github.com/peterschmidl/fdc-sds-gui")
        info.SetLicence("GPL-3.0")
        wx.adv.AboutBox(info)

    def _on_config_change(self):
        port = self._header_model.get_current_com_port()
        baud = self._header_model.parse_baudrate(self._header_model.get_current_baud_rate())
        disk_paths = {m.disk_number: m.get_path() for m in self._disk_models if m.get_path()}
        running = self._runner.run(port, baud, disk_paths, self.log_controller)
        self._header_view.set_connected(running)
