
def funcao_media ():      
    nota_ava_1 = float(input(f"{aluno.upper()}, informe a nota obtida no AVA 1: "))
    nota_ava_2 = float(input(f"{aluno.upper()}, informe a nota obtida no AVA 2: "))
    
    media = ((nota_ava_1 + nota_ava_2)/2)
    return media
    

print("Seja bem-vindo ao APROVA-ESTACIO")
print("====================================")
aluno = str(input("Aluno, informe seu nome completo: "))
if (len(aluno) < 10):
    aluno = str(input("Por gentileza, informe seu nome completo: "))
calculo = funcao_media()
print(calculo)



