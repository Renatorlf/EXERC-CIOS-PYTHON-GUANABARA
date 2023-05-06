"""
Crie um algoritimo que leia um número e mostre seu dobro, tiplo e a sua raiz quadrada.
"""
num = int(input('Digite um número: '))
d = num * 2
t = num * 3
r = num ** (1/2)

print(f'O número digitado foi {num}')
print(f'O dobro de {num} é {d}')
print(f'O tripro de {num} é {t}')
print(f'A raiz quadrada de {num} é {r:.3}')