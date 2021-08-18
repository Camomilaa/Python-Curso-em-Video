import random
choice = random.randint(0, 2)
lista = ['pedra', 'papel', 'tesoura']
print('Selecione: \n0. Pedra \n1. Papel \n2. Tesoura')
vc = int(input('Escolha: '))
esc = lista[choice]
print(f'Computador jogou {lista[choice]}')
print(f'Você jogou {lista[vc]}')

if choice == 0:
    if vc == 0:
        print(f'Empate! Ambos jogaram {lista[choice]}')
    elif vc == 1:
        print(f'Ganhou! Computador jogou {lista[choice]} e você jogou {lista[vc]}')
    elif vc == 2:
        print(f'Perdeu! Computador jogou {lista[choice]} e você jogou {lista[vc]}')
    else:
        print('Erro!')
elif choice == 1:
    if vc == 1:
        print(f'Empate! Ambos jogaram {lista[choice]}')
    elif vc == 2:
        print(f'Ganhou! Computador jogou {lista[choice]} e você jogou {lista[vc]}')
    elif vc == 0:
        print(f'Perdeu! Computador jogou {lista[choice]} e você jogou {lista[vc]}')
    else:
        print('Erro!')
elif choice == 2:
    if vc == 2:
        print(f'Empate! Ambos jogaram {lista[choice]}')
    elif vc == 0:
        print(f'Ganhou! Computador jogou {lista[choice]} e você jogou {lista[vc]}')
    elif vc == 1:
        print(f'Perdeu! Computador jogou {lista[choice]} e você jogou {lista[vc]}')
    else:
        print('Erro!')
else:
    print('Erro!')