"""
Modifique as funções que foram criadas no desafio 107 
para que elas aceitem um parâmetro a mais, 
informando se o valor retornado por elas vai ser ou não formatado pela função moeda(),
desenvolvido no desafio 108. 
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