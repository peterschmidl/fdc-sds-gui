import wx
from datetime import datetime


class LogWindow(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        self._init_ui()

    def _init_ui(self):
        sizer = wx.BoxSizer(wx.VERTICAL)
        log_label = wx.StaticText(self, label="Log")
        self.log_output = wx.TextCtrl(self, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_RICH2, size=(-1, 200))
        sizer.Add(log_label, 0, wx.ALL, 5)
        sizer.Add(self.log_output, 1, wx.EXPAND | wx.ALL, 5)
        self.SetSizer(sizer)

    def append(self, message):
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.log_output.SetInsertionPoint(0)
        self.log_output.WriteText(f"[{timestamp}] {message}\n")
