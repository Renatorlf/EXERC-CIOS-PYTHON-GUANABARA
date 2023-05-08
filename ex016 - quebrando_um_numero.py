"""
Crie um pragrama que leia um número real qualuer pelo teclaro e mostre na tela a sua porção inteira.

EX: Digite um número: 6.127
O número 6127 tem a parte inteira 6.
"""
import math
num = float(input('Digite um valor: '))
print(f'O valor digitado foi {num} e sua parte inteira é {math.trunc(num)}')