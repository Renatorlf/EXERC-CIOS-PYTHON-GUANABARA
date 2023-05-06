"""
Escreva um programa que leia um valor em metros e o exiba converntendo em centimetros e milimetros.
"""
num = float(input('Digite uma medida desejada em metros para conversão: '))


print(f'Decimetro - {num * 10:.0f}dm')
print(f'Centimetro - {num * 100:.0f}cm')
print(f'Milimetro - {num * 1000:.0f}mm')
print(f'Decâmetro - {num / 10}dam')
print(f'Hectômetro - {num / 100}hm')
print(f'Quilômetro - {num / 1000}km')

#obs. o exercício pode ser feito urilizando variáveis 