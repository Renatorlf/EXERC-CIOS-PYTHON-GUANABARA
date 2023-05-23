"""
Crie um programa que leia dois valores e mostre um menu. Seu programa deverá realizar a operação solicitada em cada caso.
[ 1 ] - somar 
[ 2 ] - Multiplicar
[ 3 ] - Maior
[ 4 ] - Novos números
[ 5 ] - Sair do programa
"""
num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
op = 0
soma = (num1 + num2)
multiplicacao = (num1 * num2)
while op!= 5:
    print('''    [ 1 ] - somar 
    [ 2 ] - Multiplicar
    [ 3 ] - Maior
    [ 4 ] - Novos números
    [ 5 ] - Sair do programa''')
    op = int(input('Digite sua opção: '))
    if op == 1:
        print(f'A soma dos dois valores é igual a {soma}.')
    elif op == 2:
        print(f'A multiplicação dos dois valores é{multiplicacao}.')
    elif op == 3:
        if num1 > num2:
            print(f'O primeiro valor {num1} é o maior.')
        if num1 == num2:
            print('Os valores digitados foram iguais.')
        else:
            print(f'O segundo valor digitado {num2} é o maior.')
    elif op == 4:
        num1 = int(input('Digite o primeiro valor: '))
        num2 = int(input('Digite o segundo valor: '))
    elif op == 5:
        print('Finalinzando...')
    else:
        print("Opção invalida digite a opção correta")
    print('=-=' * 8)
print('Obrigado por utilizar o nosso programa!')
        
    