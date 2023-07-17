"""
Crie um progama que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se o uma pessoa tem voto Negado, Opconal ou Obrigadotório nas eleições.
"""
def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'com {idade} anos:  NÃO VOTA.' 
    elif 16<= idade < 18 or idade > 65:
        return f'com idade {idade} anos: VOTO OPCIONAL.'
    else:
        return f'com idade {idade} anos: VOTO OBRIGATÓRIO'
        
nasc = int(input('Digite o ano de nascimento: '))
print(voto(nasc))
