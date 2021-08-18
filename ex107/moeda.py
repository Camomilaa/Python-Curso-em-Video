def aumentar(n):
    p = int(input('Qual a porcentagem de aumento? '))
    aum = n * (p/100)
    tot = n + aum
    print(f'Aumentando {p}% o valor aumenta para R${tot:.2f}')

def diminuir(n):
    p = int(input('Qual a porcentagem de diminuição? '))
    dim = n * (p/100)
    tot = n - dim
    print(f'Diminuindo {p}% o valor diminui para R${tot:.2f}')

def dobro(n):
    dob = n * 2
    print(f'O dobro desse valor é R${dob:.2f}')

def metade(n):
    met = n / 2
    print(f'A metade desse valor é R${met:.2f}')
