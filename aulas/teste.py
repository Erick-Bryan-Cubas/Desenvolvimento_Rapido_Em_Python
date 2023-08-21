import os
from datetime import datetime

data_e_hora_atuais = datetime.now()
mes = data_e_hora_atuais.month

tempo_colab_empresa = input(f"Informe a data de admissão ONCORP (dd/mm/aaaa):\n")

data_admissao = datetime.strptime(tempo_colab_empresa, '%d/%m/%Y')  

diff_tempo = (data_e_hora_atuais - data_admissao)

print(diff_tempo)