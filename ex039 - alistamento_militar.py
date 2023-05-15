"""
Faça um programa que leia o ano de nascimento de um jovem a informa, de acordo com sua idade. se ela "ainda vai se alistar" ao serviço militar, se é a "hora de se alistar" ou sejá "Passou do tempo" do alistamento. Seu programa também deverá mostra o tempo de falta ou que passou do prazo.
""" 
from datetime import date
atual = date.today().year
nas = int(input('Digite seu ano de nacimento: '))
sexo = str(input(' M - para masculino\n F - para feminino\n')).strip().upper()
idade = atual - nas
print(f'Sua idade é {idade} anos')
if sexo == 'F':
    print(f'Seu alistamento não é obrigatório.')
elif idade >= 18 and idade <= 45:
    print(f'Você com iddade de {idade} anos deve se alistar')
elif idade < 18 or idade > 45:
    print(f'Você com idade de {idade} anos não poderá se alitar')
"""
A obrigação para com o Serviço Militar, em tempo de paz, começa no 1º dia de janeiro do ano em que o cidadão completar 18 (dezoito) anos de idade e subsistirá até 31 de dezembro do ano em que completar 45 (quarenta e cinco) anos.
"""