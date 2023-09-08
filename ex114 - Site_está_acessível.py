"""
Crie um código em PHYTON que teste se o site Pudim está acessível pelo computador
"""
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O SITE PUDOM NÃO ESTA ACESSÍVEL NO MOMENTO!')
else:
    print('ACESSANDO O SITE PUDIM!')