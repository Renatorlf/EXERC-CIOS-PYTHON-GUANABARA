import moeda

preço = float(input('Digite o preco R$ '))
print(f'A metade de R${preço} é R${moeda.metade(preço)}')
print(f'O dobro de R${preço} é R${moeda.dobro(preço)}')
print(f'Aumentando 10%, temos R${moeda.aumentar(preço, 10):.2f}')
print(f'Diminuindo 20%, temos R${moeda.diminuir(preço, 20):.2f}')