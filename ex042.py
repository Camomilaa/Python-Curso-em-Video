a = float(input('Informe o lado A de seu triangulo: '))
b = float(input('Informe o lado B de seu triangulo: '))
c = float(input('Informe o lado C de seu triangulo: '))

if a < (b + c) and b < (a + c) and c < (b + a):
    if a == b and b == c:
        print('Equilátero')
    elif (a == b and b != c) or (a == c and c != b) or (b == c and c != a):
        print('Isósceles')
    else:
        print('Escaleno')
else:
    print('Não é triângulo')