from datetime import date

data_atual = date.today()

data_em_texto = data_atual.strftime('%d/%m/%Y')
print(data_em_texto)