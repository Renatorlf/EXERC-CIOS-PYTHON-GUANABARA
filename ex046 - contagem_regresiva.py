"""
Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio, indo de 10 até 0, com uma pauda de 1 segundo antre elas.
"""
from time import sleep
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('BUM! BUM! BUM !!!')