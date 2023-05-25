"""
Crie um programa que simula o funcionamento de um caixa eletrônico. NO início, pergunte ao usuário qual será o valor a ser sacado(Número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues 
OBS: Considere que o aixa possui cédulas de R$50, R$20, R$10 e R$1.
"""
print('=====' * 5)
print(f'        Banco RLF')
print('=====' * 5)
valor = int(input('Qual valor você deseja sacar? R$'))
total = valor
ced = 50
totCed = 0
while True:
    if total >= ced:
        total -= ced
        totCed += 1
    else:
        if totCed > 0:
            print(f'total de {totCed} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totCed = 0
        if total == 0:
            break
print('=====' * 5)
print('Volte sempre!')