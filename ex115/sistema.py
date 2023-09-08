"""
Crie um prqueno sistema modularizado que permita cadastrar pessoas
pelo seu nome e idade em um arquivo de texto simples.

O sistema só vai ter 2 opções: cadastrar uma nova pessoas e 
listar todas as pessoas cadastradas.
"""
from biblioteca.funcoes import *
from biblioteca.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)
    
while True:
    resposta = menu(['Clientes cadastrados','Cadastrar Cliente', 'Sair'])
    if resposta == 1:
        #Opçao de listar o conteúdo de um arquivo!
        lerArquivo(arq)
    elif resposta == 2:
        #opção de cadastrar uma pessoa
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Opção 3')
        break
    else:
        print('\033[31mERRO!, DIGITE UMA OPÇÃO VÁLIDA!\033[m')
    sleep(1)