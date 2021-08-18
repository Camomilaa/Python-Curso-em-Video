
def leiaInt(conf = False):
    dado = ''
    while conf == False:
        try:
            dado = int(input())
        except ValueError:
            print('O tipo digitado não é inteiro')
            print('DIGITE UM NÚMERO INTEIRO:')
        else:
            conf = True
            return dado
def leiaFloat(conf = False):
    dado = ''
    while conf == False:
        try:
            dado = float(input())
        except ValueError:
            print('\033[31mO tipo digitado não é real\033[m')
            print('DIGITE UM NÚMERO REAL:')
        else:
            conf = True
            return dado
print('DIGITE UM NÚMERO INTEIRO: ')
i = leiaInt()
print('DIGITE UM NÚMERO REAL:')
f = leiaFloat()
print(f'O NÚMERO INTEIRO DIGITADO FOI {i}, O NÚMERO REAL DIGITADO FOI {f}')