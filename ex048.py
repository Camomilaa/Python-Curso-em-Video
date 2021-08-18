soma = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
print(f'A soma de todos os multiplos de 3 é igual a {soma}')
