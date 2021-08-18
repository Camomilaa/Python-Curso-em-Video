def dobro(n):
    dob = n * 2
    return dob
def metade(n):
    met = n / 2
    return met
def aumento(p, a):
    aum = p * (a/100)
    tot = p + aum
    return tot
def dininuicao(p, r):
    dim = p * (r/100)
    tot = p - dim
    return tot
def resumo(p, a=0, r=0):
    print('-' * 60)
    print('RESUMO DO VALOR'.center(60))
    print('-' * 60)
    print(f'Preço analisado: \t\t\t\t\t\t\t\t\t R${p:.2f}'.replace('.', ','))
    print(f'Dobro do Preço: \t\t\t\t\t\t\t\t\t R${dobro(p):.2f}'.replace('.', ','))
    print(f'Metade do Preço: \t\t\t\t\t\t\t\t\t R${metade(p):.2f}'.replace('.', ','))
    print(f'Aumento de {a}%: \t\t\t\t\t\t\t\t\t R${aumento(p, a):.2f}'.replace('.', ','))
    print(f'Redução de {r}%: \t\t\t\t\t\t\t\t\t R${dininuicao(p, r):.2f}'.replace('.', ','))
    print('-' * 60)
