from datetime import date
atual = date.today().year
ano = int(input('Indique seu ano de nascimento: '))
idade = atual - ano
dano = ano + 18
falta = 18 - idade
passou = idade - 18
if idade > 18:
    print('Já passou da hora de se alistar rapazinho')
    print(f'Você está atrasado {passou} anos')
    print(f'Você deveria ter se alistado em {dano}')
elif idade == 18:
    print('Está na hora de se alistar! YEEEY')
else:
    print('Você ainda tem tempo, aproveite-o sabiamente.')
    print(f'tempo = exatamente {falta} anos')