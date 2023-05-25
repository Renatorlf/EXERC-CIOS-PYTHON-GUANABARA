"""
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final< mostre:
A) qual é o total na compra
B) quantos produtos custam mais de R$ 1000
C) qual é o nome do produto mais barato.
"""
print('+++++' * 5)
print('      Lojas Renato')
print('+++++' * 5)
total = 0
quantValores = 0
menorPreco = 0
cont = 0
nomeBarato = " "
while True:
    nomeProduto = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o valor do produto: R$ '))
    print('=====' * 6)
    cont += 1
    total += preco
    if preco > 1000:
        quantValores += 1
    if cont == 1 or preco < menorPreco:
        menorPreco = preco
        nomeBarato = nomeProduto
    '''else:
        if preco < menorPreco:
            menorPreco = preco
            nomeBarato = nomeProduto'''
  
    opcao = " " 
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    print('=====' * 6)
    if opcao == "N":
        break
print(f'O valor total da compra foi de R${total:.2f}')
print(f'A compra teve {quantValores} produtos acima de R$ 1000,00 reais.')
print(f'O produto mais barato foi {nomeBarato} que custa R$ {menorPreco:.2f}')
