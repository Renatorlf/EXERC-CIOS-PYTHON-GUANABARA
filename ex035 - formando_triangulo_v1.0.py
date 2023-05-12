"""
Desenvolva um programa que leia o comprimento de três retas e diga ao usúario se elas podem oi não formar um triângulo.
"""
print('-=' * 20)
print('Analizador de triângulos')
print('-=' * 20)
r1 = float(input('Primeiro seguimento: '))
r2 = float(input('Segundo seguimento: '))
r3 = float(input('Terceiro Seguimento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima formam um triângulo.2')
else:
    print('Os segmentos acima não formam um triângulo.')