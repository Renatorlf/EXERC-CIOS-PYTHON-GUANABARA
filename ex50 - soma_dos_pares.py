"""
Desevolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. se o valor digitado for impar descosidere-o.
"""
soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f'Você digitou {cont} números PARES e a soma foi {soma}.')
    