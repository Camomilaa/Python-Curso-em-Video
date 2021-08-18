matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = c3 = l2 = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input('Insira um número: '))
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]
            if c == 0:
                l2 = matriz[1][c]
            elif matriz[1][c] > c:
                l2 = matriz[1][c]
    c3 += matriz[l][2]
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]}]', end=' ')
    print()
print(f'A soma dos números pares da matriz é igual a {soma}')
print(f'A soma dos números da 3º coluna é igual a {c3}')
print(f'O maior valor da segunda linha é {l2}')
