maior = 0
menor = 1000
for c in range(0,5):
    peso = float(input('Informe o peso: '))
    if peso > maior:
        maior = peso
        if peso < menor:
            menor = peso
    elif peso < menor:
        menor = peso
print(f'Maior peso: {maior}\nMenor peso: {menor}')