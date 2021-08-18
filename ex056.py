totI = 0
velho = 0
mHom = ''
mulN = 0
for c in range(0, 4):
    nome = str(input('Informe o nome: '))
    idade = int(input('Informe a idade: '))
    sexo = str(input('Informe o sexo: '))

    totI += idade
    if idade > velho and sexo.upper() == 'M':
        velho = idade
        mHom = nome

    if sexo.upper() == 'F' and idade < 20:
        mulN += 1
media = totI/4
print(f'A média das idades é igual a {media:.1f} anos.')
print(f'O homem mais velho do grupo é o {mHom} com {velho} anos.')
print(f'{mulN} mulheres tem menos de 20 anos.')