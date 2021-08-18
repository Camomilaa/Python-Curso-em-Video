tot = contN = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    contN += 1
    tot += n
print(f'A quantidade de números digitados foi {contN}\nA soma total dos números equivale a {tot}')