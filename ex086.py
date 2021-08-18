ind = []
lin = []
for c in range(0,3):
    ind.append(int(input('Insira um número: ')))
    ind.append(int(input('Insira mais um número: ')))
    ind.append(int(input('Insira outro número: ')))
    lin.append(ind[:])
    ind.clear()
print(f'{lin[0]}\n{lin[1]}\n{lin[2]}')
