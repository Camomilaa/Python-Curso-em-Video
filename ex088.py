from random import randint
jogo = []
col = []
qntd = int(input('Quantos jogos deseja realizar? '))
for j in range(0, qntd):
    for n in range(0, 6):
        jogo.append(randint(1,60))
    jogo.sort()
    col.append(jogo[:])
    jogo.clear()

print(col)
