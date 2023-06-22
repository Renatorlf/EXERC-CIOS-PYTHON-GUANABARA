"""
Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros, seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""
def maior(*num):
    maior = 0
    cont = 0
    #print('-=' * 20)
    for valor in num:
        print(f'{valor}', end=' ')
        if cont == 0:
            maior == valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores.')
    print(f'O maior número encontrado foi {maior}')
    print('-=' * 20)
    
print('Analisando os valores passados...')   
maior(2, 9, 7, 3, 4, 5)
maior(3, 6, 2)
maior(1, 6)
maior(0)
maior()