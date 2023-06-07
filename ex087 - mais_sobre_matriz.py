"""
Aprimorando o exercício 86
"""
matriz = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
somaPar = 0
maior = 0
somaColuna = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c]= int(input(f'Digite um valor para [{l}, {c}]: '))

print('-=' * 15)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l] [c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            somaPar += matriz[l][c]
    print()
print('-=' * 15)
print(f'A soma dos pares é {somaPar}')
for l in range(0, 3):
    somaColuna += matriz[l][2]
print(f'A soma da ultima coluna é {somaColuna}')
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior valor da segunda linha é {maior}')