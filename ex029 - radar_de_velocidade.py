"""
Escreva um programa que leia a velocidade de um carro. Se ela ultrapassar 80km/h, mostre uma mensagem dizendi que ela foi multada.
A multa vai custar R$7.00 por cada km acima do limite de velocidade
"""
velocidade = int(input('Qual a velocidade atual do carro? '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'Voce foi multado em R$ {multa} reais!')
print('Parabéns, continue dirigindo com cuidado!')