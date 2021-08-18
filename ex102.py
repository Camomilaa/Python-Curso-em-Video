def fatorial(n, show = False):
    s = 1
    print(f'{n}! =', end=' ')
    for c in range(n,0,-1):
        if c != 1:
            s *= c
            if show == True:
                print(f'{c} x', end=' ')
        else:
            if show == True:
                print(f'{c} =', end=' ')
    print(s)
    print()
fatorial(5, True)