import moeda

preço = float(input('Digite o preco R$ '))
print(f'A metade de {moeda.moeda(preço)} é {moeda.moeda(moeda.metade(preço))}')
print(f'O dobro de {moeda.moeda(preço)} é {moeda.dobro(preço)}')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(preço, 10))}')
print(f'Diminuindo 20%, temos {moeda.moeda(moeda.diminuir(preço, 20))}')