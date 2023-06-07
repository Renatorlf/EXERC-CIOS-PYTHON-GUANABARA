"""
Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com pessoas mais pesadas.
C) Uma lista com pessoas mais leves.
"""
grupo = []
dado = []
maiorPeso = 0
menorPeso = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    '''O if neste local serve para fazer a verificação antes do valor ser inserido na lista se vai ser o maior ou o menor ''' 
    if len(grupo) == 0:
        maiorPeso = dado[1]
        menorPeso = dado[1]
    else:
        if dado[1] > maiorPeso:
            maiorPeso = dado[1]
        if dado[1] < menorPeso:
            menorPeso = dado[1]
    grupo.append(dado[:])
    dado.clear()
        
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Dejesa continuar [S/N] ')).strip().upper()[0]
    if opcao == "N":
        break
print('-=' * 30)

print(f'Ao todo foram cadastrados {len(grupo)} pessoas.')
print(f'O maior peso foi {maiorPeso}Kg de ', end= '')
#Um for fora do laço para verificar o maior peso
for p in grupo:
    if p[1] == maiorPeso:
        print(f'{p[0]}',  end=' ')
print(f'\nO menor peso foi {menorPeso}Kg de', end=' ')
#outro for fora do laço While para verificar o menor peso
for p in grupo:
    if p[1] == menorPeso:
        print(f'{p[0]}', end=' ') 
