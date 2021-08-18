jogador = dict()
gols = 0
jogador['nome'] = str(input('Nome: '))
jogador['partidas'] = int(input('Partidas Jogadas: '))
for c in range(0,jogador['partidas']):
    gols += int(input(f'Quantos gols realizados na partida {c+1}? '))
jogador['gols'] = gols
jogador['aproveitamento'] = gols/jogador['partidas']
for k,v in jogador.items():
    if k != 'aproveitamento':
        print(f'{k}: {v}')
    else:
        print(f'O {k} é de {v:.1f} gols por partida')