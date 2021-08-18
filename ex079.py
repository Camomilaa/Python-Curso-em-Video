nums = []
while True:
    n = int(input('Digite um número: '))
    if n not in nums:
        nums.append(n)
    cont = str(input('Deseja continuar? [S/N] ')).upper()
    if cont == 'N':
        break
nums.sort()
print(nums)
