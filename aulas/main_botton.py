import wx   # Importa o módulo wxPython
import wx.grid as gridlib  # Importa o módulo gridlib
import wx

class SampleFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Cores e Tamanhos', size=(300, 300))
        # Criando um painel
        panel = wx.Panel(self)
        # Criando o grid com 4 linhas e 1 coluna com 5 px de espaço ao redor
        grid = wx.GridSizer(4, 1, 5, 5)
        text = wx.TextCtrl(panel, size=(150, -1))
        enter_button = wx.Button(panel, label='Enviar')
        label = wx.StaticText(panel, label='Bem vindo')
        message_button = wx.Button(panel, label='Mostrar mensagem')
        # Add os botões ao grid
        grid.AddMany([text, enter_button, label, message_button])
        panel.SetSizer(grid) 
                      
class MainApp(wx.App):
    def OnInit(self):
        frames = SampleFrame()
        frames.Show()
        return True
    
app = MainApp()
app.MainLoop()