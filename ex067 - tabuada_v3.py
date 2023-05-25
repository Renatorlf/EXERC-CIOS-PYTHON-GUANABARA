"""
Faça uma tabuada que mostre a tabuada de vários números. um de cada vez. para cada valor digitadi pelo usuário, O programa será interrompido quando o número solicitado for negativo.
"""
num = 0
while True:
    print('-=' * 19)
    num = int(input('Quer ver a tabuada de qual número? '))
    print('-=' * 19)
    if num < 0:
        break
    for c in range(1, 11):
        print(f'{c} X {num} = {num * c}')
print('FIM!!')