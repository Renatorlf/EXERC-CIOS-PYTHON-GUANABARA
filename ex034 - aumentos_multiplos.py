"""
Escreva um programa que pergunte o saláro de um funcionário e calcule o valor do seu aumento.
Para salário superior a R$ 1.250, calcule um aumento de 10%.
para os inferiores ou iguais, o aumento é de 15%
"""
salario = float(input('Digite o valor do salário: '))
valor1 = salario + (salario * 15/100)
valor2 = salario + (salario * 10/100)
if salario > 1250:
    print(f'O valor do seu salário passará a ser de R${valor2}')
else:
    print(f'O valor do seu salario agora será de R${valor1}')