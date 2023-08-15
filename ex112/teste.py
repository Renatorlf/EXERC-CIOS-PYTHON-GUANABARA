"""
Dentro do pacote utilidadesCeV que criamos no desafio 111,
termo um módulo chamdo dado. Crie uma função chamada leiaDinheiro()
que seja capaz de funcionar como a função input(), mas com uma
Validação de dados para aceitar apenas valore que sejam monetários.
"""
from utilidadesCeV import moeda
from utilidadesCeV import dado

preço = dado.leiaDinheiro('Digite o preço: R$')
moeda.resumo(preço, 10, 10)