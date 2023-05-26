"""
Crie um programa que vai gurar cinco número aleatórios e colocar em uma tupla, depois disso, mostre a listagem de número gerados e também indique o menor e o maior valor que estão na tupla
"""
import random
numeros = (random.randint(1, 5), random.randint(1, 5),random.randint(1, 5),random.randint(1, 5),random.randint(1, 5),)
print('Os valores sorteados foram ', end=' ')
for n in numeros:
    print(f'{n}', end='')
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')