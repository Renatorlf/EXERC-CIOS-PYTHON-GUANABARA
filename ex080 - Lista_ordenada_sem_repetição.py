"""
Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sorted()). No final, mostre a lista ordenada na tela.
"""
lista = []

for v in range(0, 5): #V de valor
    num = int(input('Digite um valor: '))
    '''if num not in lista:
        lista.append(num)
    elif num in lista:
        print('Valor já adicionado') ''' 
    if v == 0 or num > lista[-1]:
        lista.append(num)
        print('Adcionado ao final da lista')
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                print(f'Adicionado na posição {pos}')
                break
            pos += 1        
print('-=' * 25)
print(f'os valores digitados em orden foram {lista}')


