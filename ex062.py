pt = int(input('Indique o Primeiro termo da PA: '))
r = int(input('Indique a razão da PA: '))
c = 1
print(f'{pt}', end=' ')
while c != 10:
    pt = pt + r
    print(f'{pt}', end=' ')
    c += 1
banana = 0
while banana != 1: #Banana é o controlador dos 'mais termos?'
    print('\nDeseja mostrar mais termos?')
    qnt = int(input('Quantos? '))
    if qnt == 0:
        banana = 1
    c2 = 0
    while c2 != qnt:
        pt = pt + r
        print(f'{pt}', end=' ')
        c2 += 1

