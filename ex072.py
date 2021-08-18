num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
       'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze',
       'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    vc = int(input('Insira um número de 0 a 20: '))
    if vc > 20:
        print('Erro!')
        break
    else:
        print(num[vc])
