import math
multi = 0
num = int(input('Digite o número: '))
for c in range(2, num):
    if num % c == 0:
        multi += 1
        prim = 2
    elif multi == 0:
        prim = 1
if prim == 1:
    print(f'{num} é um número primo')
elif prim == 2:
    print(f'{num} não é um número primo')


