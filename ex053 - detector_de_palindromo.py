"""
Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços.
"""
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('Temos um palíndromo')
else:
    print('Não temos um palíndromo!')