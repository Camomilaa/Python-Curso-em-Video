from random import randint
c = 0
pc = randint(0, 10)
vc = int(input('Advinhe qual número de 0 a 10 o computador está pensando: \n'))
if vc == pc:
    print('Uau... de primeira!')
else:
    while vc != pc:
        if vc > pc:
            print('QUASEE! tente um número menor!')
        else:
            print('QUASEE! tente um número maior!')
        vc = int(input('ERROU! Tente de novo: '))
        c += 1
    c += 1
    print(f'Finalmente... Você precisou de {c} tentativas')