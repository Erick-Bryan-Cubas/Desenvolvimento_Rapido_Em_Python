import wx

class Buttons(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Buttons', size=(300, 200))
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)  # Main vertical box sizer

        # Nome
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        label1 = wx.StaticText(panel, label='Nome')
        text_ctrl1 = wx.TextCtrl(panel)
        hbox1.Add(label1, 0, wx.ALL, 5)
        hbox1.Add(text_ctrl1, 1, wx.ALL, 5)
        vbox.Add(hbox1, 0, wx.EXPAND | wx.ALL, 5)

        # Idade
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        label2 = wx.StaticText(panel, label='Age')
        text_ctrl2 = wx.TextCtrl(panel)
        hbox2.Add(label2, 0, wx.ALL, 5)
        hbox2.Add(text_ctrl2, 1, wx.ALL, 5)
        vbox.Add(hbox2, 0, wx.EXPAND | wx.ALL, 5)

        # Enter Button
        enter_button = wx.Button(panel, label='Enter')
        vbox.Add(enter_button, 0, wx.ALL | wx.ALIGN_LEFT, 5)
        
        # Welcome Label
        welcome_label = wx.StaticText(panel, label='Welcome')
        vbox.Add(welcome_label, 0, wx.ALL | wx.ALIGN_LEFT, 5)
        
        # Birthday Button
        message_button = wx.Button(panel, label='Birthday')
        vbox.Add(message_button, 0, wx.ALL | wx.ALIGN_LEFT, 5)

        panel.SetSizer(vbox)

class MainApp(wx.App):
    def OnInit(self):
        frame = Buttons()
        frame.Show()
        return True
        
app = MainApp()
app.MainLoop()
