"""
Crie um programa que leia vários núeros inteiros peloo teclado. O programa só vai para quando o usúario digitar o valor 999, que é a condição de parada. no final, mostre quantos número foram digitados e qual foi a soma entre eles(disconsiderando o flag).
"""
num = 0
cont = 0
soma = 0
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    cont += 1
    soma += num
    num = int(input('Digite um número [999 para parar]: '))
print(f'Você digitou {cont} números e a soma entre eles foi {soma}')

