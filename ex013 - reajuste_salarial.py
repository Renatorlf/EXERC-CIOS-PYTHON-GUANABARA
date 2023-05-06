"""
Faça um programa que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
"""
salario = float(input('Digite o valor do salário atual R$'))
novo_salario = salario + (salario * 15/100)

print(f'Seu novo salário agora é de R${novo_salario}')