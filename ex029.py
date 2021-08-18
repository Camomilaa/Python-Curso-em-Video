vel = float(input('Digite a velocidade indicada: '))
crime = vel - 80
multa = crime * 7
if vel > 80:
    print(f'Você foi multado! Pague imediatamente o valor de R${multa:.2f}')
else:
    print('Vrum vrum')
