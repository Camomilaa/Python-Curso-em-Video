numsP = []
numsI = []
nums = []
while True:
    nums.append(int(input('Digite um número: ')))
    cont = str(input('Deseja continuar? [S/N] ')).upper()
    if cont == 'N':
        break
for c in nums:
    if c % 2 == 0:
        numsP.append(c)
    else:
        numsI.append(c)
print(f'Todos os números:\n{nums}')
print(f'Números pares: \n{numsP}')
print(f'Números ímpares: \n{numsI}')