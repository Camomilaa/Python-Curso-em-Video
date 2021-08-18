pes = list()
fic = list()
pesa = lev = 0
while True:
    pes.append(str(input('Digite o nome: ')))
    pes.append(int(input('Digite o peso: ')))
    if len(fic) == 0:
        pesa = lev = pes[1]
    else:
        if pes[1] > pesa:
            pesa = pes[1]
        elif pes[1] < lev:
            lev = pes[1]
    fic.append(pes[:])
    pes.clear()
    cont = str(input('Deseja continuar? [S/N] ')).upper()
    if cont == 'N':
        break
print(f'Foram cadastradas {len(fic)} pessoas')
print(f'A pessoa mais pesada tem {pesa:.2f}', end=' ')
for p in fic:
    if pesa == p[1]:
        print(f'e seu nome é {p[0]}')
print(f'\nA pessoa mais leve tem {lev:.2f}', end=' ')
for p in fic:
    if lev == p[1]:
        print(f'e seu nome é {p[0]}')