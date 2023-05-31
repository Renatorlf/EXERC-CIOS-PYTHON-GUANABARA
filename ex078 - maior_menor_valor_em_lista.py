"""
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e suas respectivas posições na lista.
"""
lista = []
#lista fazia para receber os valores
for cont in range(0, 5):
    #for para fazer o laço com range
    num = lista.append(input(f'Digite um valor na posição {cont}: '))
    #Uma variavel para receber os valores e o append para adicionar na lista fazia
print('-=' * 25)
print(f'O maior número da lista é {max(lista)} nos índeces ', end='')
#um print com max para mostrar o maior valor da lista
for i, v in enumerate(lista):
    #for com duas variáveis uma para o índice (i) e outra #para mostrar os valores (v) e o enumerate para enumerar os índices.
    if lista[i] == max(lista):
        print(i, end='...')
print(f'\nO menor número da lista é {min(lista)} nos índices ', end='')
for i, v in enumerate(lista):
    if lista[i] == min(lista):
        print(i, end='...')
    