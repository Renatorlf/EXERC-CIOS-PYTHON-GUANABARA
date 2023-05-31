"""
Crie um programa que bai ler vários número e colocar em uma lista. Depois disso, crie duas litas extras que vão conter os valorespares e os valores impares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
"""
lista = []
pares = []
impares = []
while True:
    num = int(input('Digite um valor: '))
    lista.append(num)
    if num % 2 == 0:
        pares.append(num)
    elif num % 2 == 1:
        impares.append(num)
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar [S/N]')).strip().upper()[0]
    if opcao == 'N':
        break
    
print(f'Lista completa é {lista}')
print(f'Lista de pares {pares}')
print(f'Lista de impares {impares}')