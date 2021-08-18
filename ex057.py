sexo = str(input('Qual seu sexo? [M/F]')).upper()
while sexo != 'M'and sexo != 'F':
    sexo = str(input('Qual seu sexo? [M/F]')).upper()
if sexo == 'M':
    print('Bem-vindo!')
else:
    print('Bem-vinda!')