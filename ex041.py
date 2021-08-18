from datetime import date
atual = date.today().year
ano = int(input('Insira seu ano de nascimento: '))
idade = atual - ano
if idade <= 9:
    print('Mirim')
elif idade <= 14:
    print('Infantil')
elif idade <= 19:
    print('Junior')
elif idade <= 25:
    print('Sênior')
else:
    print('Master')