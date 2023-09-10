# ESCREVA UM PROGRAMA QUE CRIA UM RELATÓRIO DE USUÁRIO. SEU PROGRAMA DEVE RECEBER DADOS DO USUÁRIO E ARMAZENAR EM UM NOVO ARQUIVO COM O NOME DO USUÁRIO. ESSE ARQUIVO DEVE SER SALVO EM UMA PASTA COM A DATA DO DIA.

from pathlib import Path
from datetime import date

pasta = Path.cwd()
pasta = pasta / 'relatorios'
pasta.mkdir(exist_ok=True)

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
profissao = input('Digite sua profissão: ')
frase_do_dia = input('Digite sua frase do dia: ')

data = date.today()
nome_arquivo = f'{nome}_{data}.txt'
arquivo = pasta / nome_arquivo

arquivo.write_text(f'Nome: {nome}\nIdade: {idade}\nProfissão: {profissao}\nFrase do dia: {frase_do_dia}')