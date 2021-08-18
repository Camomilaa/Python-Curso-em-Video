pal = ('Aprender', 'Sonhar', 'Lutar', 'Gatinho', 'Seixas')
for p in pal:
    print(f'\nNa palavra {p.upper()} temos', end=' ')
    for l in p:
        if l.lower() in 'aeiou':
            print(l.upper(), end=' ')
