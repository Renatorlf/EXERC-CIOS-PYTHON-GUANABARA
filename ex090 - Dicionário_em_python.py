"""
Faça um programa que leia nome e média de um aluno, guardando também a stuação em um dicionário> no final, mostre o conteúdo da extrutura na tela.
"""
aluno = {}

aluno['nome'] = str(input('Digite o nome do aluno: ')) 
aluno['media'] = float(input('Digite a média do aluno: '))

print('-=' * 20)
print(f'- O nome do aluno é {aluno["nome"]}')
print(f'- A media do aluno é {aluno["media"]}')
if aluno['media'] <= 5:
    '''coloquei está adição da situação só para lembrar que pode fezer desta forma, mas não necessita colocar.'''
    aluno['situação'] = 'Reprovado'
    print(f'- O aluno {aluno["nome"]} está REPROVADO!')
elif aluno['media'] > 5 and aluno['media'] < 7:
    aluno['situação'] = 'Recuperação'
    print(f'- O aluno {aluno["nome"]} está em RECUPERAÇÃO!')
else:
    aluno['situação'] = 'Aprovado'
    print(f'- O aluno {aluno["nome"]} está APROVADO!')
     