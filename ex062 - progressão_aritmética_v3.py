"""
Melhorando o DESAFIO 061, perguntando para o usuáreo se ele quer mostrar mais alguns termo. O programa ecerra quando ele disser que quer mostrar 0 termo.
"""
print('gerenciador de PA')
print('-=' * 10)
primeiro = int(input('Primiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(termo, end=' -> ')
        termo += razao
        cont += 1
    print('PAUSA!!')
    mais = int(input('Mostrar quantos termos a mais? '))
print('FIM!!')
print(f'A PA teve ao todo {total} termos')