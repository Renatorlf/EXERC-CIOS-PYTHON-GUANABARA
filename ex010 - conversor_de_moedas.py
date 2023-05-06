"""
Faça um programa que pergunte quanto uma pessoa tem na carteira e mostre quantos dolares ela pode comprar.
"""
real = float(input('Quanto de dinheiro você tem na carteira? '))
dolar = (real / 4.49)

print(f'Com este dinheiro da para comprar US${dolar:.2f} dolares!')