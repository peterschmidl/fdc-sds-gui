import wx


class DiskWindow(wx.Panel):
    def __init__(self, parent, disk_number):
        super().__init__(parent)
        self.controller = None
        self._init_ui(disk_number)

    def _init_ui(self, disk_number):
        box = wx.StaticBox(self, label=f"Disk {disk_number}")
        sizer = wx.StaticBoxSizer(box, wx.VERTICAL)

        self.path_text = wx.TextCtrl(self, style=wx.TE_READONLY)

        btn_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.load_button = wx.Button(self, label="Load")
        self.unload_button = wx.Button(self, label="Unload")
        btn_sizer.Add(self.load_button, 1, wx.ALL, 2)
        btn_sizer.Add(self.unload_button, 1, wx.ALL, 2)

        sizer.Add(self.path_text, 0, wx.EXPAND | wx.ALL, 5)
        sizer.Add(btn_sizer, 0, wx.EXPAND | wx.ALL, 2)
        self.SetSizer(sizer)

    def set_controller(self, controller):
        self.controller = controller
        self.load_button.Bind(wx.EVT_BUTTON, lambda e: controller.handle_load_click())
        self.unload_button.Bind(wx.EVT_BUTTON, lambda e: controller.handle_unload_click())

    def get_path(self):
        with wx.FileDialog(self, "Select Altair Disk Image to load",
                           wildcard="Disk Images (*.dsk)|*.dsk",
                           style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as dlg:
            if dlg.ShowModal() == wx.ID_OK:
                return dlg.GetPath()
        return ""

    def set_path(self, path):
        self.path_text.SetValue(path)
