"""
esvreva um programa que leia um número qualquer e peça para o osuário escolher qualquer será a base de conversão:
"""
print('-=' * 20)
print(f'{(" " * 5)}Conversor de Base Númerica')
print('-=' * 20)

num = int(input('Digite um numero: '))

print('\n[1] - Binário')
print('[2] - octal')
print('[3] - hexadecimal')

op = int(input(f'\nEscolha uma opção sua conversão: '))

if op == 1:
    print(f'O número {num} convertido para BINÁRIO é igual a {bin(num)}')

elif op == 2:
    print(f'O número {num} convertido para OCTAL é igual a {oct(num)}')
    
elif op == 3:
    print(f'O número {num} convertido para HEXADECIMAL é igual a {hex(num)}')
else:
    print('Digite a opção correta!')