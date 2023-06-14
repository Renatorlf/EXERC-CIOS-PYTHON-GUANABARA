"""
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada em um dicionário e todos os dicionários em uma lista. No final, mostre:
A)Quantas pessoas cadastradas
B)A média de idade.
C)Uma Lista com mulheres.
D)Uma lista com idade acima da média. 
"""
galera = []
pessoa = {}
soma = 0
media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! apenas M ou F')  
    pessoa['idade'] = int(input('Idade: '))
    galera.append(pessoa.copy())
    soma += pessoa['idade']
    while True:
        resp = str(input('Deseja continuar [S/N]')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERROR! apenas S ou N')
    if resp == 'N':
        break
print('-=' * 20)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'B) A media das idades é de {media:.2f} anos.')
print(f'C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] == 'F': #não foi utulizado (in) porque utilizamos upper()
        print(f'{p["nome"]} ', end='')
print(f'\nD) Lista de pessoas que estão a cima da média: ')
for p in galera:
    if p['idade'] >= media:
        for k, v in p.items():
            print(f'{k} = {v}. ', end='')
        print()
print('<< ENCERRADO >>')