"""
Crie um programa que leia o ano de nascimento de sete pessoas. no final. mostre quantas pesssoas ainda não atingiram a maioridade e quantas já são maiores.
"""
from datetime import date
ano_atual = date.today().year
totmaior = 0
totmenor = 0
for c in range(1, 8):
    ano = int(input(f'Em que ano a {c}ª pessoa nasceu? '))
    idade = ano_atual - ano
    if idade >= 18:
        totmaior += 1
    else:
        totmenor += 1
print(f'{totmaior} pessoas são maiores de idade.')
print(f'{totmenor} pessoas são menores de idade.')