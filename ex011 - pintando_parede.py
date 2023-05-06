"""
Faça um progrema que leia a altura e a largura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que a cada litro da tinta, pinta uma área de 2m².
"""
largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))

area = (altura * largura)
tinta = area / 2
print(f'Sua parede tem a dimessão de {altura}X{largura} e sua área e de {area}m²')
print(f'Para pintar a sua parede você necessita de {tinta}L de tinta.')
