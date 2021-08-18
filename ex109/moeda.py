def aumentar(n,c = False):
    p = int(input('Qual a porcentagem de aumento? '))
    aum = n * (p/100)
    tot = n + aum
    if c == False:
        print(f'Aumentando {p}% o valor aumenta para R${tot:.2f}')
    else:
        print(f'Aumentando {p}% o valor aumenta para R${tot:.2f}'.replace('.',','))

def diminuir(n, c = False):
    p = int(input('Qual a porcentagem de diminuição? '))
    dim = n * (p/100)
    tot = n - dim
    if c == False:
        print(f'Diminuindo {p}% o valor diminui para R${tot:.2f}')
    else:
        print(f'Diminuindo {p}% o valor diminui para R${tot:.2f}'.replace('.',','))

def dobro(n, c = False):
    dob = n * 2
    if c == False:
        print(f'O dobro desse valor é R${dob:.2f}')
    else:
        print(f'O dobro desse valor é R${dob:.2f}'.replace('.',','))

def metade(n, c = False):
    met = n / 2
    if c == False:
        print(f'A metade desse valor é R${met:.2f}')
    else:
        print(f'A metade desse valor é R${met:.2f}'.replace('.',','))
