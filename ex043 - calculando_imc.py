"""
desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
- abaixo de 18.5: abaixo do peso
- entre 18.5 e 25: peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade mórbida"""
altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
imc = peso / (altura ** 2)
print(f'O IMC dessa pessoa é de {imc:.2f}')

if imc < 18.5:
    print('ABAIXO DO PESO!')
elif imc >= 18.5 and imc < 25: #modo tradicional
#elif 18.5 <= imc < 25: simplificado
    print('PESO IDEAL!')
elif imc >= 25 and imc < 30: #modo tradicional
#elif 25 <= imc < 30: simplificado 
    print('SOBRE PESO!')
elif imc >= 30 and imc < 40: #modo tradicional
#elif 30 <= imc < 40: simplificado
    print('OBESIDADE!')
else:
    print('OBESIDADE MÓRBIDA!')
    