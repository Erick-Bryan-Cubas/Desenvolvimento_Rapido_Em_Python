def funcao_media ():      
    nota_ava_1 = float(input(f"{aluno.upper()}, informe a nota obtida no AVA 1: "))
    nota_ava_2 = float(input(f"{aluno.upper()}, informe a nota obtida no AVA 2: "))
    
    media = ((nota_ava_1 + nota_ava_2)/2)
    return media
    

print("Seja bem-vindo ao APROVA-ESTACIO")
print("="*40)
aluno = str(input("Aluno, informe seu nome completo: "))
if (len(aluno)) < 10:
    aluno = str(input("Por gentileza, informe seu nome completo: "))
calculo = funcao_media()

if(calculo < 5):
    print(f""" Média no curso de DESENVOLVIMENTO RÁPIDO EM PYTHON: {calculo}
          {aluno.upper()}, infelizmente sua média não foi o suficiente para ser aprovado no curso. Tente novamente! """)
elif(calculo <= 5 or calculo < 7):
    print(f""" Média no curso de DESENVOLVIMENTO RÁPIDO EM PYTHON: {calculo}
          {aluno.upper()}, sua média não foi o suficiente para ser aprovado. Contudo, está em recuperação. Boa sorte! """)
else:
    print(f""" Média no curso de DESENVOLVIMENTO RÁPIDO EM PYTHON: {calculo}
          {aluno.upper()}, parabéns pela aprovação no curso! """)

    



