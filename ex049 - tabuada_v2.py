"""
Refaça o Desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
"""
num = int(input('Digite um número para a mostrrar a tabuada: '))
for c in range(1, 11):
    """multiplicacao = (num * c)
    print(f'{num} X {c} = {multiplicacao}')
    você pode fazer desta forma"""
    print(f'{num} X {c} = {num * c}') #Ou desta forma