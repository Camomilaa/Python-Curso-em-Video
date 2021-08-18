peso = float(input('Indique seu peso: '))
altura = float(input('Indique sua altura: '))
imc = peso / (altura**2)
if imc < 18.5:
    print('Abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print('Peso Ideal')
elif imc >= 25 and imc < 30:
    print('Sobrepeso')
elif imc >= 30 and imc <= 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')
print(f'Seu imc é: {imc:.2f}')