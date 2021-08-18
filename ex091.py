from random import randint
from operator import itemgetter
ranking = list()
jogos = {
    'jogador 1': randint(1, 6),
    'jogador 2': randint(1, 6),
    'jogador 3': randint(1, 6),
    'jogador 4': randint(1, 6)
}
for k, v in jogos.items():
    print(f'{k} tirou {v} no dado')
ranking = sorted(jogos.items(), key=itemgetter(1), reverse=True)
print(ranking)
for n, i in enumerate(ranking):
    print(f'{n+1}º lugar: {i[0]} com {i[1]} pontos')