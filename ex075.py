nums = (int(input('Insira um número: ')),
        int(input('Insira um número: ')),
        int(input('Insira um número: ')),
        int(input('Insira um número: ')))
nove = 0
pares = ''
spc = ' '
for c in range(0,4):
    if nums[c] == 9:
        nove += 1
    elif nums[c] % 2 == 0:
        pares += str(nums[c])
        if c != 3:
            pares += spc
if nove == 0:
    print('Não foi encontrado nenhum número 9')
elif nove == 1:
    print('Foi encontrado apenas 1 número 9')
else:
    print(f'Foram encontrados {nove} números 9')
if 3 in nums:
    print(f'Número 3 encontrado na posição {nums.index(3) + 1}')
else:
    print('Não foi encontrado número 3')
print(f'Os números pares encontrados foram: {pares}')
