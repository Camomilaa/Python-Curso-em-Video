while True:
    num = int(input('Digite um número: '))
    c = 0
    if num < 0:
        break
    while c < 11:
        print(f'{num} x {c} = {num*c}')
        c += 1