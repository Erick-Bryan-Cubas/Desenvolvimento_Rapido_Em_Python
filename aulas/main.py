import wx




# Criando a aplicação de um objeto
app = wx.App()
# Criando uma tela
frame = wx.Frame(parent=None, title='Primeira tela')
# Adicionando um texto a tela
text = wx.StaticText(parent=frame, label='Hello, world!')
# Mostrando a tela
frame.Show()
# Executando a função principal
app.MainLoop()
