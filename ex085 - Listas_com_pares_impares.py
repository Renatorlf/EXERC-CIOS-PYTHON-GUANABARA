"""
Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e impares. No final, mostre os valores pares e ímpares em ordem crescente.
"""
principal = [[], []]
valor = 0
for c in range(1, 8):
    valor = (int(input(f'Digite o {c}º número: ')))  
    if valor % 2 == 0:
        principal[0].append(valor)
    else:
        principal[1].append(valor)
print('-=' * 30)
print(f'Os valores pares digitados foram {sorted(principal[0])}')
print(f'Os valores ímpares digitados foram {sorted(principal[1])}')