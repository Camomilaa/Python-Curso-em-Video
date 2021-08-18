jogador = dict()
time = list()
while True:
    gols = 0
    jogador['nome'] = str(input('Nome: '))
    jogador['partidas'] = int(input('Partidas Jogadas: '))
    for c in range(0, jogador['partidas']):
        gols += int(input(f'Quantos gols realizados na partida {c + 1}? '))
    jogador['total'] = gols
    jogador['aproveitamento'] = gols/jogador['partidas']
    time.append(jogador.copy())
    jogador.clear()

    cont = str(input('Deseja continuar? ')).upper()
    if cont == 'N':
        break
while True:
    qual = int(input('Qual o número do jogador que deseja checar? '))
    for c, j in enumerate(time):
        if qual == c:
            print(f'{c}- {j["nome"]} \n{j["partidas"]} partidas jogadas\n{j["aproveitamento"]:.1f} de aproveitamento')

