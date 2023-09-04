import wx

class MainApp(wx.App):
    def OnInit(self):
        frame = wx.Frame(parent=None, title='Primeira tela')
        text = wx.StaticText(parent=frame, label='Hello, world!')
        frame.Show()
        return True
app = MainApp()
app.MainLoop()