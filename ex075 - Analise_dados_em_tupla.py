"""
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final mostre:
A)Quantas vezes apareceu o valor 9.
8)Em qual posição foi digitado o primeiro valor 3
C)Quais foram os números pares.
"""

num = (int(input('Digite o primeiro valor: ')),
       int(input('Digite o primeiro valor: ')),
       int(input('Digite o primeiro valor: ')),
       int(input('Digite o primeiro valor: ')))
print(f'Você digitou os seguintes valores {num}')
print(f'O número 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O número 3 apareceu na posicão {num.index(3)+1}')
else:
    print('O número 3 não foi digitado')
print(f'O números pares digitados foram ', end='')
for par in num:
    if par % 2 == 0:
        print(par, end=' ')
