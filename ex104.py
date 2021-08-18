def leiaInt(n, sla = False):
    print(n, end='')
    n = input()
    if n.isnumeric():
        sla = True
        return n
    while sla == False:
        n = leiaInt('Digite um número: ')
        if n.isnumeric():
            sla = True
            return n
n = leiaInt('Digite um número: ')
print(f'Você digitou {n}')