from math import hypot
cat1 = float(input('Insira o valor do primeiro cateto: '))
cat2 = float(input('Insira o valor do segundo cateto: '))
hip = hypot(cat1, cat2)
print('O valor da hipotenusa é {:.2f}'.format(hip))