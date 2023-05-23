"""
Crie um programa que leia vários número inteiros pelo teclaro. No final da execução, mostre a média entre todos e os valores e qual foi o maior e o menor valores lidos. O programa deve peruntar ao usuário se ele quer ou não continuar a digitar valores. 
"""
opcao = 'S'
media = 0
quant = 0
soma = 0
maior = 0
menor = 0
while opcao == 'S':
    num = int(input('Digite um número: '))
    opcao = str(input('Você quer continuar? [S/N] ')).upper().strip()[0]
    soma += num
    quant += 1
    
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
media = (soma / quant)
print(f'A quantidade de número digitados foi {quant} e a média foi {media:.2f}')
print(f'O Maior número digitado foi {maior} e o menor foi {menor}')
print('ACABOU!!')
