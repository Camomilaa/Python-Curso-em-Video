p = []
i = []
t = []
for x in range(0,7):
    n = int(input('Insira um número: '))
    if n % 2 == 0:
        p.append(n)
    else:
        i.append(n)
t.append(p)
t.append(i)
t.sort()
print(t)