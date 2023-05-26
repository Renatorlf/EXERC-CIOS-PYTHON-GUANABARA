"""
Crie um Programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tubular.
"""
listagem =('lapis', 1.75,
           'Borracha', 2.00,
           'Caderno', 15.99, 
           'Estojo', 25.00, 
           'Transferidor',4.20, 
           'Compasso', 9.99,
           'Mochila', 120.32)
print('-' * 40)
print(F'{"Listagem de preços":^40}')
print('-' * 40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:.2f}')
print('-' * 40)
    