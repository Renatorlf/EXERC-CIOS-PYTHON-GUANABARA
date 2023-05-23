"""
Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos de uma progressão usando a estrutura while.
"""
print('gerenciador de PA')
print('-=' * 10)
primeiro = int(input('Primiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(termo, end=' -> ')
    termo += razao
    cont += 1
print('FIM!!')