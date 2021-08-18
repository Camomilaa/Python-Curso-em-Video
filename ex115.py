import datetime
td = list()
def menu():
    print('-' * 30)
    print('\033[33m' + 'MENU PRINCIPAL'.center(30) + '\033[0;0m')
    print('-' * 30)
    print('\033[32m' + '1. Ver pessoas cadastradas' + '\033[0;0m')
    print('\033[34m' + '2. Cadastrar nova Pessoa' + '\033[0;0m')
    print('\033[35m' + '3. Sair do Sistema' + '\033[0;0m')
    print('-' * 30)
def cadastro():
    pessoas = dict()
    pessoas['nome'] = str(input('Insira o nome da pessoa cadastrada: '))
    ano = int(input('Data de nascimento '))
    pessoas['idade'] = datetime.datetime.now().year - ano
    pessoas['genero'] = str(input('Genero: [F/M] ')).upper()
    td.append(pessoas.copy())
    pessoas.clear()
def checar():
    op2 = str(input('Deseja checar uma pessoa em especifico? [S/N] ')).upper()
    if op2 == 'N':
        print(td)
    else:
        op3 = int(input('Número da pessoa que deseja checar: '))
        print(f'Nome: {td[op3]["nome"]}\nIdade: {td[op3]["idade"]}\nGenero: {td[op3]["genero"]}')
while True:
    menu()
    op = int(input('Sua opção: '))
    try:
        if op == 1:
            checar()
        elif op == 2:
            cadastro()
        elif op == 3:
            break
        else:
            print('\033[31m' + 'Digite uma opção válida' '\033[0;0m')
    except ValueError:
        print('O caractere digitado não corresponde a um número inteiro válido!')