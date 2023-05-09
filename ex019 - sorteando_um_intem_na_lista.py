"""
Um professor quer sorteras um dos seus aquatro alunos para apagar o quadro. Faça um programa que ajude ele. lendo o nome delas e escrevendo o nome do escolhido
"""
import random
a1 = str(input('Digite o nome do primeiro aluno: '))
a2 = str(input('Digite o nome do segundo aluno: '))
a3 = str(input('digite o nome do terceiro aluno: '))
a4 = str(input('Digite o nome do quarto aluno: '))
lista = [a1, a2, a3, a4]
escolhido = random.choice(lista)
print(f'O aluno escolhido foi {escolhido}')
 