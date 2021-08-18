pt = int(input('Indique o Primeiro termo da PA: '))
r = int(input('Indique a razão da PA: '))
for c in range(pt, pt + (r * 10), r):
    print(c, end='  ')