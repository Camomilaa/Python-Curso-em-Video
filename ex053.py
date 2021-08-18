frase = str(input('Digite a frase: ')).strip().upper()
separado = frase.split()
junto = ''.join(separado)
inverso = ''

for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('Palíndromo')
else:
    print('Não é palíndromo')

