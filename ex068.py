from random import choice, randint
vit = per = 0
poi = ['par', 'impar']
while True:
    pc = choice(poi)
    break
print(f'Pc é {pc}')
if pc == 'par':
    print('Você é ímpar')
    v = 'impar'
else:
    print('Você é par')
    v = 'par'
while True:
   while True:
       pc2 = randint(1, 10)
       break
   num = int(input('Digite um número: '))
   print(f'Pc escolheu {pc2}')
   print(f'{num} + {pc2} = {num + pc2}')
   if (num + pc2) % 2 == 0:
       if v == 'par':
           print('Você venceu!')
           vit += 1
       else:
           print('Você perdeu!')
           break
   else:
       if v == 'impar':
           print('Você venceu!')
           vit += 1
       else:
           print('Você perdeu!')
           break
print(f'Você venceu {vit} vezes')
