pt = int(input('Indique o Primeiro termo da PA: '))
r = int(input('Indique a razão da PA: '))
c = 1
print(f'{pt}', end=' ')
while c != 10:
    pt = pt + r
    print(f'{pt}', end=' ')
    c += 1