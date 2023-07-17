"""
Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai restonar um dicionário com as seguintes informações:
- Quantidade de notas
- A maior nota 
- A menor nota
- A média da turma 
- A situação (opcional)
- Adicionar também as docstrings.
"""
def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :parametro n: uma ou mais notas dos alunos (aceita várias)
    :parametro sit: valor opcional, indicando se deve ou não adicionar a situação
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r
    
resp = notas(5.5, 2.5, 9, 8.5, sit=True)
print(resp)