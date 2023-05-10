"""
Faça um programa que leia uma frase pelo tecaro e mostre:
- Qauntas vezes aparece a letra 'A'.
- em que posição ela aparece e a primera vez.
= em que posição ela aparece a última vez.
"""
frase = str(input('Digite uma frase: ')).strip().upper()
print('A letra A aparece {} vezes na frase'.format(frase.count("A")))
print(f'A primeira letra A apareceu na posição {frase.find("A")+1}')
#Este +1 é utilizado para deixar a posição da forma que a gente lê.
print(f'A ultima letra A apareceu na posição {frase.rfind("A")+1}')