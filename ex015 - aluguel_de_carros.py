"""
Escreva um programa que pergunte a quantidade de Km percorrido po um carro alugado e a quantidade de dias pelos quais foi alugado. Calcule o preço a pagar. sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado
"""

dias = int(input('Digite a quantidade de dias: '))
km = float(input('Digite a quilometragem percorrida: '))

aluguel = (dias * 60) + (km * 0.15)

print(f'O Valor a pagar pelo aluguel do véiculo é de R${aluguel:.2f}')
