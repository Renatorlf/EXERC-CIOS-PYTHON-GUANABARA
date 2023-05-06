"""
Faça um programa que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
"""
produto = float(input('Digite o valor do produto. R$ '))
desconto = produto - (produto * 5/100)

print(f'O valor do produto sem desconto é R$ {produto}')
print(f'O valor do produto com desconto de 5% é de R$ {desconto:.2f}')