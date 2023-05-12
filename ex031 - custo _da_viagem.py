"""
Deselvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem. cobrando R$0.50 por km para viagens de até 200km e R$0.45 para viagens mais longas
"""
"""
existem várias forma de fazer este exercício, uma delas com duas variáveis como as que estão em comentário,
utilizando também o calculo com variável o if e no else, e com eu fiz com o calculo dentro do print.
"""
distancia = int(input('Qual a distância em Km da viagem? '))
#km1 = distancia * 0.50
#km2 = distancia * 0.45

if distancia <= 200:
    print(f'O valor da sua passagem será R$ {distancia * 0.50}')
else:
    print(f'O valor da passagem com preço promocinal será R$ {distancia * 0.45}')
print('Aproveite a viagem e se divirta.')