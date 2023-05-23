"""
Melhore o jogo do DESAFIO 028 ondeo o computador vai pensar em um número entre 0 e 10. Só que agora o jogador vai tentar advinhar até acertar, mostrando no final quantos palpites foram necessários para vencer
"""
from random import randint
computador = randint(0, 10)
print('Sou seu computador... estou pensando em um número entre 0 e 10.')
print('tenta Advinhar!!')

acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Esta cehagndo perto!!')
        elif jogador > computador:
            print('Menos... esta quase acertando!!')
print(f'Você acertou com {palpites} tentativ as.')
