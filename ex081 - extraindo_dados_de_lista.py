"""
 Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
 A) Quantos número foram digitados.
 B) A lista de valores, ordenada de forma decrescente.
 C) Se o calor 5 foi digitado e está ou não na lista.
"""
lista = []
while True:
    num = lista.append(int(input('Digite um valor: ')))
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input(('Deseja continuar [S/N]'))).strip().upper()[0]
    if opcao == 'N':
        break
    
print('-=' * 30)
print(f'Você digitou {len(lista)} elementos')
lista.sort(reverse=True)
print(f'A lista em forma decrescente é {lista}')
if 5 in lista:
    print('O número 5 está contido na lista')
else:
    print('O número 5 não está contido na lista')  