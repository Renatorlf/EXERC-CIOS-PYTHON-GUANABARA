"""
Adicione ao módulo moeda.py criado nos desafios anteriores,uma função chamada resumo(),
que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.
"""
def aumentar(preço=0, taxa=0, formatado=False):
    res = preço + (preço * taxa/100)
    return res if formatado is False else moeda(res)
    
def diminuir(preço=0, taxa=0, formatado=False):
    res = preço - (preço * taxa/100)
    return res if formatado is False else moeda(res)
    
def dobro(preço=0, formatado=False):
    res = preço * 2
    return res if not formatado else moeda(res)
    #forma diferente de representara mesma escrita de cima
    
def metade(preço=0, formatado=False):
    res = preço / 2
    return res if not formatado else moeda(res)
    #forma diferente de representara mesma escrita de cima

def moeda(preço=0, moeda=   'R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')

def resumo(preço=0, taxaa=10, taxar=5):
    print('-' * 30)
    print(f'RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analizado: \t{moeda(preço)}')
    print(f'Dobro do preco:  \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(preço, taxaa, True)}')
    print(f'{taxar}% de redução: \t\t{diminuir(preço, taxar, True)}')
    