"""
Escreva um programa que faça o computador "PENSAR" em um número inteiro e esntre 0 e 5 e peça para o usúario tentar descobrir que foi o número escolhio pelo computador. 0 programa deverará escrever na tela se o usuario venceu ou perdeu.
"""
import random
from time import sleep
computador = random.randint(0, 5) #faz o computador sortear

print('-=-' * 20)
print('Vamos jogar ?') 
print('tente advinhar o númer que o computador entre 0 e 5')
print('-=-' * 20)
jogador = int(input('Eu penseu no número: '))
print('Processando...')
sleep(3)
if jogador == computador:
    print('Parabéns, Você acertou!')
else:
    print('Você não acertou!!')
print('Vamos jogar de novo?')