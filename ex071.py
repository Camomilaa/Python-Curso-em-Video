saque = int(input('Qual será o valor do saque? '))
totsaque = saque
n50 = n20 = n10 = n1 = 0
while True:
    if saque > 50:
        n50 += 1
        saque -= 50
    elif saque > 20:
        n20 += 1
        saque -= 20
    elif saque > 10:
        n10 += 1
        saque -= 10
    elif saque >= 1:
        n1 += 1
        saque -= 1
    else:
        break
print(f'O saque será realizado em {n50} notas de 50, {n20} notas de 20, {n10} notas de 10 e {n1} moedas de 1')
print(f'Total: R${totsaque:.2f}')
