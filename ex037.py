num = int(input('Digite seu número: '))
print(' 1. Binário \n 2. Octal \n 3. Hexadecimal')
esc = int(input('Escolha: '))
if esc == 1:
    print(f'{num} em binário é igual a {bin(num) [2:]}')
elif esc == 2:
    print(f'{num} em octal é igual a {oct(num) [2:]}')
elif esc == 3:
    print(f'{num} em hexadecimal é igual a {hex(num) [2:]}')
