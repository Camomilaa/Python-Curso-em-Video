nums = (int(input('Insira um número: ')),
        int(input('Insira um número: ')),
        int(input('Insira um número: ')),
        int(input('Insira um número: ')))
print(f'Foram encontrados {nums.count(9)} números 9')
if nums.__contains__(3):
    print(f'Número 3 encontrado na posição {nums.index(3) + 1}')
else:
    print('Não foi encontrado número 3')
print(f'Os números pares encontrados foram:')
for c in range(0,4):
    if nums[c] % 2 == 0:
        print(nums[c], end=' ')