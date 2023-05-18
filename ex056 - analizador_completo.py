"""
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. no final do programa, mostre:
- A média de idade do grupo.
- Qual é o nome do homem mais velho.
- Quantas mulheres têm menos de 20 anos.
"""
somaIdade = 0
mediaIdade = 0
idadeVelho = 0
nomeVelho = " "
totmulher = 0
for p in range(1, 5):
    print(f'------{p}ª Pessoa ------')
    nome = str(input('Nome: ')).strip().upper()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    somaIdade += idade
    if p == 1 and sexo in 'M':
        idadeVelho = idade
        nomeVelho = nome
    if sexo in 'M' and idade > idadeVelho:
        idadeVelho = idade
        nomeVelho = nome
    if  sexo in 'F' and idade < 20:
        totmulher += 1
        

mediaIdade = somaIdade / 4
print(f'A media dde idade é de {mediaIdade}anos')
print(f'O homem mais velho tem {idadeVelho} anos e se chama {nomeVelho}')
print(f'{totmulher}mulheres com menos de 20 anos.')
