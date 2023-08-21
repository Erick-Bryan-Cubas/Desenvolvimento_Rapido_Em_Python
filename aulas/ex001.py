import os
from datetime import datetime




print("Seja-bem vindo ao ONCRED")
usuario = input("Por gentileza, informe seu nome: ")
if(len(usuario)< 4):
  usuario = input("O nome deve ser maior que 4 caracteres, digite novamente: ")


tipo_pessoa =  int(input(f"{usuario.upper()}, informe se é pessoa física (PF) ou jurídica!: Digite 1 para PF e 2 para PJ: "))

if(tipo_pessoa == 1):
  tipo_pessoa = False
  validador_tipo_pf = int(input(f"""{usuario.upper()}, selecionou TIPO PESSOA FÍSICA, tem certeza da seleção? 
                                Se sim, digite 1(um) para prosseguir e 0(zero) para voltar  """))

  if(validador_tipo_pf == 1):
    print("TIPO PESSOA FÍSICA selecionada e confirmada!")
    
    tempo_colab_empresa = input(f"{usuario.upper()}, informe a data de admissão ONCORP (dd/mm/aaaa):\n")
    
    data_admissao = datetime.strptime(tempo_colab_empresa, '%d/%m/%Y')  
    data_e_hora_atuais = datetime.now()
    
    diff_tempo = (data_e_hora_atuais - data_admissao)
    diff_days = diff_tempo.days
    tempo_min_credito = (90 - diff_days)
    
    
    if(diff_days <= 90):
        print(f'{usuario.upper()} retorne após {tempo_min_credito} dias para uma nova análise.')
        
        
       # print('Liberado um cartão de crédito da conta correspondente (PF) com limite de 40% da sua renda/faturamento')
        