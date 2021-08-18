frase = str(input('Digite a frase: ')).upper()
fra = frase.replace(' ','').replace('-','')
inverso = ''
for letra in range(len(fra) - 1, -1, -1):
    inverso += fra[letra]

if fra == inverso:
    print('Palíndromo')
else:
    print('Não é palíndromo')