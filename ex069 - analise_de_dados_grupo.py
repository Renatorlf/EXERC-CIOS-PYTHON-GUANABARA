"""
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrad, o programa deverá perguntar se o usuário quer ou não continuar. No filnal, mostre:
A) quantas pessoas te mais de 18 anos
B) Quantos homens foram cadastrados.
C) Quantas mulherestem menos de 20 anos.
"""
tot18 = 0
totH = 0
totM20 = 0
while True:
    print('=' * 25)
    print ('  CADASTRE UMA PESSOA')
    print('=' * 25)
    idade = int(input('idade: '))
    sexo = " "
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    print('=' * 25)
    if idade >= 18:
        tot18 += 1
    if sexo == "M":
        totH += 1
    if sexo == "F" and idade < 20:
        totM20 += 1
    opcao = " "
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]   
    if opcao == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {totH} homens cadastrados:')
print(f'Temos {totM20} mulheres com menos de 20 anos.')