"""
Escreva em programa que leia dois números inteiros e compare-os mostrando na tela uma mensagem:
- O primeiro número é maior
- O segundo número é maior
- Os dois números são iguais
"""
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

if num1 > num2:
    print(f'O primeiro número é maior')

elif num2 > num1:
    print(f'O segundo número é maior')
else:
    print(f'Os dois números são iguais')    