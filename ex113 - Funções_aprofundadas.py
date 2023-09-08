"""
Reescreva a função leiaint() que fisemos no desafio 104,
incluindo agora a possibilidade de digitação de um número do tipo inválido.
Aproveite e crie também uma função leiafloat() com a mesma funcionalidade.
"""
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError, KeyboardInterrupt):
            print('\033[31mERRO: Por favor digite um número inteiro válido?\033[m')
        else: 
            return n
        
def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError, TypeError, KeyboardInterrupt):
            print('\033[31mPor favor digite um número real válido!\033[m')
        else:
            return n

num1 = leiaInt('Digite um valor inteiro: ')
num2 = leiaFloat('Digite um valor real: ')
print(f'O número real digitado foi {num1} e o real foi {num2}')