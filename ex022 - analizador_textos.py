"""
Crie um progrma que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sm considerar os espaços).
- Quantas letras tem o primeiro nome.
"""
nome = str(input('Digite seu nome: ')).strip()
print(f'Seu nome em maiúsculo é {nome.upper()}')
print(f'Seu nome em minúsculo é {nome.lower()}')
print(f'Seu nome tem ao todo {len(nome) - nome.count(" ")} caracteres')
print(f'Seu primeiro nome tem {nome.find(" ")} letras')
