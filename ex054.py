from datetime import date
maior = 0
menor = 0
for c in range(0,7):
    ano = int(input('Informe o ano de nascimento: '))
    if (date.today().year - ano) >= 18:
        maior += 1
    else:
        menor += 1
print(f'{menor} menores de idade\n{maior} maiores de idade')