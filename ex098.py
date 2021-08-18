def contador(ini, fim, passo):
    for c in range(ini, fim, passo):
        print(c, end=' ')
    print()

contador(1,10,1)
contador(10,0,-1)
i = int(input('Digite o ínicio: '))
f = int(input('Digite o fim: '))
p = int(input('Digite o passo: '))
contador(i,f,p)