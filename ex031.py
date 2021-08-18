dis = float(input('Distancia: '))
if dis <= 200:
    val = 0.5 * dis
    print(f'O valor é {val:.2f}')
else:
    val = 0.45 * dis
    print(f'O valor é {val:.2f}')
