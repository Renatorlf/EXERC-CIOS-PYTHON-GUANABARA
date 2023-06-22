"""
Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retandular (largura e comprimento) e mostre a aréa do terreno.
"""

def area(largura, comprimento):
    multi = (largura * comprimento)
    print(f'A área de um terreno {largura} X {comprimento} é de {multi}')
    
# programa principal
print('    Controle de Terreno')
print('-=' * 30)
largura = float(input('Digite a largura do terreno: '))
comprimento = float(input('Digite o comprimento do terreno: '))
area(largura, comprimento)