"""
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.
"""
sexo = str(input('Digite M ou F para o sexo: ')).strip().upper()
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite corretamente M ou F para o sexo: ')).strip().upper()
print('FIM!!')
