"""
Elabore um programa que cacule o valor a ser pago por um produto, considerando o seu preço normal e condições de pagamneto:
- À vista dinheiro/cheque: 10% de desconto.
- À vist no cartão: 5% de desconto
- Em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros.
"""
preco = float(input('Valor das compras: R$ '))
print('FORMA DE PAGAMENTO')
print(' [ 1 ] à vista dinheiro/cheque\n [ 2 ] à vista no debito\n [ 3 ] 2x no cartão credito\n [ 4 ] 3x ou mais no credito')
opcao = int(input('Opção: '))

if opcao == 1:
    desconto = preco - (preco * 10/100)
    print(f'Valor a ser pago R$ {desconto:.2f}')
    print('OBRIGADO POR COMPRAR EM NOSSAS LOJAS!')
elif opcao == 2:
    desconto = preco - (preco * 5/100)
    print(f'Valor a ser pago R$ {desconto:.2f}')
    print('OBRIGADO POR COMPRAR EM NOSSAS LOJAS!')
elif opcao == 3:
    total = (preco / 2) 
    print(f'Valor a ser pago será duas parcelas de R$ {total:.2f}')
    print('OBRIGADO POR COMPRAR EM NOSSAS LOJAS!')
elif opcao == 4:
    """
    eu utilizei um looping while para poder pedir ao usuário que ele digite o número de parcelas novamente caso o usuário digite o número de parcelas errodo.
    """
    while True:
        print('Acima de 3 parcelas e no máximo 10.')
        parcelas = int(input('Em quantas parcelas?: '))
        if parcelas > 3 and parcelas < 10:
            total = (preco + (preco * 20 / 100)) / parcelas
            print(f'Valor a ser pago será {parcelas} de R$ {total:.2f} ')
            print('OBRIGADO POR COMPRAR EM NOSSAS LOJAS!')
            break
        else:
            print('Digite o número correrto de parcelas')