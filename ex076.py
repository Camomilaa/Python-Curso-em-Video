prod = ('Gás', '120.00', 'Shampoo', '20.00', 'Duzia de ovos', '15.50', 'Par de meia', '10.00')
c = 0
print('='*37)
print('LISTA DE COMPRAS')
print('='*37)
while True:
    if c % 2 == 0:
        print(f'{prod[c]:.<30} R$ {prod[c + 1]}')
    c += 1
    if c == len(prod):
        break
