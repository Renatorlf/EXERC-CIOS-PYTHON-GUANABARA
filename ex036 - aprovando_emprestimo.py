"""
escreva um programa para aprovar o empréstimo bancário para compra de uma casa. Pergunte o valor da casa, o salário do compradore em quantos anos ele vai pagar.
A prestação mensal, não pode exceder 30% do salário ou netão o empréstimo será negado.
"""
casa = float(input('Valor da casa: R$ '))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestacao = casa / (anos * 12)
print(f'Para quitar a casa em {anos} anos o valor da prestação fica de R$ {prestacao:.2f}')
if prestacao > (salario * 30/100):
    print(f'Empréstimo negado, valor da prestação de R$ {prestacao:.2f} excede 30% do seu salário.')
else:
    print(f'Empréstimo aprovado, Parabéns por adquirir sua casa própria.')