"""
Faça um programa que leia aldo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possivéis sobre ela.
"""

a = input('Digite algo: ')
print(f'O tipo primitivo deste valor é {type(a)}')
print('Tem espaço? ', a.isspace())
print('É um número? ', a.isnumeric())
print('É alfabetico? ', a.isalpha())
print('É alfanumerico? ', a.isalnum())
print('Está em maiuscula?', a.isupper())
print('Está em miniscula?', a.islower())
print('Esta capitalizado?', a.istitle())
