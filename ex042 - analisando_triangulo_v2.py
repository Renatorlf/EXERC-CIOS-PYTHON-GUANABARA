"""
Refaça o Desafio 0 35 dos trinângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓCELES: dois lados iguais
- ESCALENO: todos os lados diferentes
"""
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + 2:
    print('Os segmentos acima PODEM FORMAR um triângulo.')
    if r1 == r2 == r3:
        print(f'Os raios formam um triângulo EQUILÁTERO.')
    elif r1 != r2 != r3 != r1:
        print(f'Os raios formam um triângulo ESCALENO')
    else:
        print('os raios formam um triângulo ISÓSCELES')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo.')