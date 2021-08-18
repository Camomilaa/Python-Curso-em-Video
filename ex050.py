soma = 0
n = []
for c in range(1, 7):
    num = int(input('Insira um número: '))
    n.append(num)
    if num % 2 == 0:
        soma += num
print(f'O valor da soma é igual a {soma}')
