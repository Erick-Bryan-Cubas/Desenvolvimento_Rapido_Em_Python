import wx

class SampleFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Cores e Tamanhos', size=(300, 300))
        
        self.panel1 = wx.Panel(self)
        self.panel1.SetSize(300, 100)
        self.panel1.SetBackgroundColour(wx.Colour(255, 0, 0))
        
        self.panel2 = wx.Panel(self)
        self.panel2.SetSize(1, 110, 300, 100)
        self.panel2.SetBackgroundColour(wx.Colour(255, 0, 0))
        
class MainApp(wx.App):
    def OnInit(self):
        frames = SampleFrame()
        frames.Show()
        return True
    
app = MainApp()
app.MainLoop()