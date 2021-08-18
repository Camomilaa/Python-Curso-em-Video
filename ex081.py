nums = []
c = 0
while True:
    nums.append(int(input('Digite um número: ')))
    cont = str(input('Deseja continuar? [S/N] ')).upper()
    c += 1
    if cont == 'N':
        break
nums.sort(reverse=True)
print(f'Foram digitados {c} números.')
print(nums)
if 5 in nums:
    print(f'Número 5 se encontra na lista', end=' Posição/ões:')
    for p, n in enumerate(nums):
        if n == 5:
            print(f'{p}', end=' ')
else:
    print('Número 5 não se encontra')
