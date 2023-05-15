"""
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atinginda:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO 
"""
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('digite a terceira nota: '))
media = (nota1 + nota2 + nota3) / 3
if media >= 7.0:
    print(f'Sua media é {media:.1f} e você está APROVADO!')
elif media >= 5.0 and media < 7:
    print(f'Sua média é {media:.1f} e você está de RECUPERAÇÃO.')
elif media < 5:
    print(f'Sua média é {media:.1f} e você está REPROVADO')