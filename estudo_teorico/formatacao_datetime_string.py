from datetime import date

# Formatação com 'f-string'
data_atual = date.today()
data_f_string = f"{data_atual.day}/{data_atual.month}/{data_atual.year}"
print(data_f_string)

# Formatação com format
data_format = '{}/{}/{}'.format(data_atual.day, data_atual.month, data_atual.year)
print(data_format)