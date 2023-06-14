"""
Aprimore o exercício 93 par que ele funcione com vários jogadores, incluindo um sitema de visualização de detalhes do aproveitamento de cada jogador.
"""
#VARIÁVEIS
jogador = {}
golsPartida = []
time = []

#PROCESSAMENTO\
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do joador: '))
    totPartidas = int(input(f'O {jogador["nome"]} jogou quantas partidas? '))
    golsPartida.clear()
    for c in range(0, totPartidas):
        golsPartida.append(int(input(f'Quantos Gols o {jogador["nome"]} fez na {c+1}ª partida? ')))
    jogador['gols'] = golsPartida[:]
    jogador['total'] = sum(golsPartida)
    time.append(jogador.copy())
    
    while True:
        resp = str(input('Deseja continuar [S/N]')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! penas S ou N')
    if resp == 'N':
        break

#SAÍDA e analise de dados
print('-=' * 20)
print('cod', end=' ')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-=' * 20)
for k, v in enumerate(time):
    print(f'{k+1:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15} ', end='')
    print()
print('-=' * 20)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar)  '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! não existe este jogador com este código {busca}')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}: ')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    no jogo {i+1} fez {g} gols.')
    print('-' * 45 )
print('<< VOLTE SEMPRE >>')

