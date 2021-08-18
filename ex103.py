def ficha(nome, gols = 0):
    print(f'O jogador {nome} fez {gols} gols no campeonato!')
n = input('Qual o nome do jogador? ')
g = input('Quantos gols ele fez no campeonato? ')
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha('DESCONHECIDO', g)
else:
    ficha(n,g)