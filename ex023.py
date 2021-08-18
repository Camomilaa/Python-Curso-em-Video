num = int(input('Digite um numero: '))
u = num % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))