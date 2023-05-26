"""
Crie um programa que tnha uma tupla totalment preenchida com uma contagem por extenso, de zero até vinte.

Seu programa deverá ler um número pelo teclado(entre 0 e 20)
e mostra-lo por extenso.
"""
extenso = ('ZERO','UM','DOIS','TRÊS','QUATRO','CINCO','SEIS','SETE','OITO','NOVE','DEZ','ONZE','DOZE','TREZE','CATORZE','QUINZE','DEZESSEIS','DEZESSETE','DEZITO','DEZENOVE','VINTE')

# exemplo1
'''numero = int(input('Digite um número entre (0, 20): '))
while numero not in range(0, 21):
    numero = int(input('digite um número entre (0, 20): '))
print(f'Você digitou o numero {extenso[numero]}.')'''


while True:
    numero = int(input('Digite um número: '))
    if 0 <= numero <= 20:
        print(f'Você digitou o número {extenso[numero]}')
    
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Deseja continuer [S/N] ')).strip().upper()[0]
    if opcao == 'N':
        break
print('FIM!!')