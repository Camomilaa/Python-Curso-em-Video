import random
n = random.randint(0,5)
num = int(input('Tente adivinhar o número entre 0 e 5 em que o computador está pensando: '))
if n == num:
    print('Parabens, você acertou! O número era {}!'.format(num))
else:
    print('Que pena... O número era {} e você disse {}'.format(n, num))