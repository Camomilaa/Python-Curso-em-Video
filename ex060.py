n = int(input('Digite um número: '))
print(f'{n}! =  {n}', end=' ')
result = n
while n > 0:
    n = n - 1
    print(f'x {n}', end=' ')
    if n != 0:
        result *= n

print(f' = {result}')
