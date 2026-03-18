import wx
from helpers import Helpers


class LedIndicator(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent, size=(24, 24))
        self._on = False
        self.Bind(wx.EVT_PAINT, self._on_paint)

    def _on_paint(self, _event):
        dc = wx.PaintDC(self)
        dc.SetBackground(wx.Brush(self.GetParent().GetBackgroundColour()))
        dc.Clear()
        color = wx.Colour(0, 200, 0) if self._on else wx.Colour(80, 80, 80)
        dc.SetBrush(wx.Brush(color))
        dc.SetPen(wx.Pen(wx.Colour(0, 0, 0), 1))
        dc.DrawCircle(12, 12, 10)

    def setValue(self, state):
        self._on = state
        self.Refresh()


class HeaderWindow(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        self._init_ui()

    def _init_ui(self):
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.ports_label = wx.StaticText(self, label="Serial Port")
        self.ports = wx.ComboBox(self, style=wx.CB_READONLY)
        self.baud_rates_label = wx.StaticText(self, label="Baud Rate")
        self.baud_rates = wx.ComboBox(self, style=wx.CB_READONLY)
        self.connected = LedIndicator(self)

        sizer.Add(self.ports_label, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        sizer.Add(self.ports, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        sizer.Add(self.baud_rates_label, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        sizer.Add(self.baud_rates, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        sizer.Add(self.connected, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        self.SetSizer(sizer)

    def populate_baud_rates(self, baud_rates):
        self.baud_rates.Clear()
        self.baud_rates.AppendItems(baud_rates)

    def populate_com_ports(self, com_ports):
        self.ports.Clear()
        self.ports.AppendItems(com_ports)

    def set_current_baud_rate(self, index):
        self.baud_rates.SetSelection(index)

    def set_current_com_port(self, index):
        self.ports.SetSelection(index)

    def get_selected_port(self):
        return self.ports.GetValue()

    def get_selected_baud_rate(self):
        return self.baud_rates.GetValue()

    def set_connected(self, state):
        self.connected.setValue(state)

    def set_controller(self, controller):
        self.controller = controller
        self.ports.Bind(wx.EVT_COMBOBOX, lambda e: controller.handle_com_port_change())
        self.baud_rates.Bind(wx.EVT_COMBOBOX, lambda e: controller.handle_baudrate_change())
