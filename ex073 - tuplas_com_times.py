"""
Crie uma tupla preenchida com os 20 times da serie A do campeonato Brasileiro na ordem de colocação. Depois mostre:
A)Os 5 primeiros
B)Os 4 últimos colocados.
C)Times na ordem alfabética.
D)Em que posição está o time do São Paulo
"""
times = ('Botafogo','Palmeiras','Fluminense','Atlético-MG','Cruzeiro','Flamengo','Atlético-PR','São Paulo','Santos','Grêmio','Fortaleza','Bragantino','bahia','Cuiabá-MT','Internacional','Goiás','Vasco da Gama','Corinthians','America-MG','Coritiba')
print('-=-=-=' * 10)
print(f'Lista de times do Brasileirão: {times}')
print('-=-=-=' * 10)
print(f'Os 5 primeiros times são {times[0:5]}')
print('-=-=-=' * 10)
print(f'Os 4 útimos são {times[-4:]}')
print('-=-=-=' * 10)
print(f'times em ordem alfabética {sorted(times)}')
print('-=-=-=' * 10)
print(f'O São paulo esta na {times.index("São Paulo")}ª posição')