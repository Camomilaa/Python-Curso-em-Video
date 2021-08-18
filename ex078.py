nums = []
for c in range(0,5):
    nums.append(int(input('Digite um número: ')))
for c, v in enumerate(nums):
    if c == 0:
        maior = menor = nums[0]
    else:
        if v > maior:
            maior = v
        elif v < menor:
            menor = v
print(f'O maior valor digitado foi {maior} na posição', end=' ')
for c, v in enumerate(nums):
    if v == maior:
        print(f'{c} ', end='.. ')
print(f'\nO menor valor foi {menor} na posição', end=' ')
for c, v in enumerate(nums):
    if v == menor:
        print(f'{c} ', end='.. ')