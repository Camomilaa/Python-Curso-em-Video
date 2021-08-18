frase = str(input('Digite sua frase: ')).strip().upper()
print('A quantidade de vezes em que a letra A aparece é {}'. format(frase.upper().count('A')))
print('A posição em que ela aparece pela primeira vez é: {}'.format(frase.find('A') + 1))
print('A posição em que ela aparece pela ultima vez é: {}'.format((frase.rfind('A') + 1)))