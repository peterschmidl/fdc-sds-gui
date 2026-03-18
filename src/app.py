import sys
import shutil
import os
from pathlib import Path
import wx
from views.main_window import MainWindow

app = wx.App()

#if not sys.platform.startswith('darwin') and not sys.platform.startswith('linux'):
#    wx.MessageBox('Unsupported platform (Linux and MacOS are supported)', 'FDC-SDS-GUI Error', wx.ICON_ERROR)
#    sys.exit(1)

_submodule_binary = Path(__file__).resolve().parents[1] / "external/fdc-sds/fdcsds"

if getattr(sys, 'frozen', False):
    fdcsds_path = str(Path(sys._MEIPASS) / 'fdcsds')
    os.chmod(fdcsds_path, 0o755)
    os.environ['FDCSDS_PATH'] = fdcsds_path
elif _submodule_binary.is_file():
    os.environ['FDCSDS_PATH'] = str(_submodule_binary)
elif shutil.which("fdcsds"):
    os.environ['FDCSDS_PATH'] = shutil.which("fdcsds")
else:
    wx.MessageBox(
        'fdcsds command not found in PATH.\nPlease install FDC-SDS Serial Disk Server\n(https://github.com/deltecent/fdc-sds)',
        'FDC-SDS-GUI Error', wx.ICON_ERROR
    )
    #sys.exit(1)

window = MainWindow()
window.Show()

app.MainLoop()
