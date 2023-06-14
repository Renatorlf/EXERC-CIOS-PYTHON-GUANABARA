"""
Cries um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depos vai ler a quantidade de gols feitos em cada pertida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
"""
jogador = {}
golsPartida = []
jogador['nome'] = str(input('Nome do joador: '))
totPartidas = int(input(f'O {jogador["nome"]} jogou quantas partidas? '))
for c in range(0, totPartidas):
    golsPartida.append(int(input(f'Quantos Gols o {jogador["nome"]} fez na {c+1}ª partida? ')))
jogador['gols'] = golsPartida
jogador['total_gols'] = sum(golsPartida)
print('-=' * 20)
print(jogador)
print('-=' * 20)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 20)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partida.')
for c, i in enumerate(jogador['gols']):
    print(f'   => Na partida {c+1}ª, o {jogador["nome"]} fez {i} gols.')
print(f'Foi um total de {jogador["total_gols"]} gols.')