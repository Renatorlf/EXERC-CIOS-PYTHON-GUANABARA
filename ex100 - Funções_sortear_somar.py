"""
Faça um programa que tenha uma lista chamada números e duas fuções chamdas sortear() e somarP(). A primeira função vai sorter 5 número e vai colocá-los dentro da litsa e a segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior.
"""
from random import randint
from time import sleep
def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        n = randint(0, 10)
        lista.append(n)
        print(f'{n}', end=' - ', flush=True)
        sleep(0.5)
    print('PRONTO!')

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'somando os números pares da lista {lista}, temos {soma}')

numero = []
sorteia(numero)
somaPar(numero)


    