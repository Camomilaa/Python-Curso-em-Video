resp = ''
soma = quantV = 0
while resp != 'N':
    n = int(input('Digite um número: '))
    soma += n
    quantV += 1
    if quantV == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Deseja continuar? [S/N] ')).upper()
media = soma / quantV
print(f'A média de valores foi {media}\nO maior valor foi {maior}\nO menor valor foi {menor}')