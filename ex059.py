n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
c = 0
while c != 5:
    print('[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa')
    c = int(input('Escolha uma opção acima:'))
    if c == 1:
        soma = n1 + n2
        print(f'{n1} + {n2} = {soma}')
    elif c == 2:
        mult = n1 * n2
        print(f'{n1} * {n2} = {mult}')
    elif c == 3:
        if n1 > n2:
            print(f'{n1} é o maior!')
        else:
            print(f'{n2} é o maior!')
    elif c == 4:
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
    else:
        print('ERRO!')
        break

