a = float(input('Indique o lado A de seu triângulo: '))
b = float(input('Indique o lado B de seu triângulo: '))
c = float(input('Indique o lado C de seu triângulo: '))

if a < (b + c) and b < (a + c) and c < (b + a):
    print('Pode sim ser um triângulo')
else:
    print('Não pode ser triangulo')