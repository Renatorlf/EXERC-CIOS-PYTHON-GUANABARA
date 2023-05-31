"""
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Casoo número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
"""
lista = []
while True:
    num = int(input('Digite um valor: '))
    if num not in lista:
        lista.append(num)
        print('Valor adicionado')
    else:
        print('Valor repetido não pode ser adicionado')
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar [S/N] ')).strip().upper()[0]
    if opcao == 'N':
        break
print('-=' * 20)
print(f'Os valores adicionados na lista foram {sorted(lista)}')
print('FIM!!')