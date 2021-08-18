from random import randint
num = list()
def sorteia():
    for c in range(0,5):
        num.append(randint(0,9))
    print(num)
def somaPar():
    s = 0
    for n in num:
        if n % 2 == 0:
            s += n
    print(f'A soma equivale a {s}')
sorteia()
somaPar()