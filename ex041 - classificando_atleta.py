"""
A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUVENIL
- até 25 anos: ADULTO
- Acima: MASTER
"""
from datetime import date
nascimento = int(input('Digite seu ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - nascimento
print(f'O atleta tem {idade} anos')
if idade <= 9:
    print('O atleta se enquadra na categoria MIRIM.')
elif idade <= 14:
    print('O atleta se enquadra na categoria INFANTIL.')
elif idade <= 19:
    print('O atleta se encaixa na categoria JUVENIL.')
elif idade <= 25:
    print('O atleta se encaixa na categoria ADULTO.')
else:
    print('O atleta se encaixa na categoria MASTER.')
