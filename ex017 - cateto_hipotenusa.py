"""
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retãngulo. calcule e mostre o comprimento da hipotenusa.
"""
import math
cat_oposto = float(input('Comprimento do cateto oposto: '))
cat_adjacente = float(input('comprimento do cateto adjacente: '))
hipotenusa = math.hypot(cat_oposto, cat_adjacente)

print(f'A hipotenusa vai medir {hipotenusa:.2f}')
