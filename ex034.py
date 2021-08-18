sal = float(input('Digite o valor do seu salário: '))
if sal > 1250:
    nsal = sal + (sal * 0.1)
    print(f'Seu novo salário é igual a R${nsal:.2f}')
else:
    nsal = sal + (sal * 0.15)
    print(f'Seu novo salário é igual a R${nsal:.2f}')
