"""
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. nor final, mostre um boletim conetendo a média de cada um e permita que o usúario possa mostrar as notas de cada aluno individualmente. 
"""
ficha = []

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    
    opcao = ' '
    while opcao not in 'NS':
        opcao = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    if opcao == 'N':
        break
print('-=' * 20)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for i, a in enumerate(ficha):
    print(f'{i+1:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 20)
    opc = int(input('Você quer ver a nota de qual aluno? (0 - interrompe): '))
    if opc == 0:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')