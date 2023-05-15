"""
Crie um programa que faça o computador jogar JoKepô com você.
"""
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Sua opções:
[ 0 ] PEDRA 
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é sua jogada? '))
print('JÔ')
sleep(1)
print('KE')
sleep(1)
print('PÔ!!!')
print('-=' * 11)
print(f'Computador jogou {itens[computador]}')
print(f'Você jogou {itens[jogador]}')
print('-=' * 11)

if computador == 0: #computador jogou PEDRA
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('JOGADOR VENCE!')
    elif jogador == 2:
        print('COMPUTADOR VENCE!')
    else:
        print('JOGADAR INVÁLIDA!')
    
elif computador == 1: #computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE!') 
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2: 
        print('JOGADOR VENCE!')
    else:
        print('JOGADAR INVÁLIDA!')
    
elif computador == 2: #computador jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCE!')
    elif jogador == 1:
        print('COMPUTADOR VENCE!')
    elif jogador == 2:
        print('EMPATE!')  
    else:
        print('JOGADAR INVÁLIDA!')
        