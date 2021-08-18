'''Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando
 os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas B) A média de idade
C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média'''

pes = dict()
mult = list()
mul = list()
maior = list()
tot = 0
while True:
    pes['nome'] = str(input('Nome: '))
    pes['sexo'] = str(input('Sexo: ')).upper()
    pes['idade'] = int(input('Idade: '))
    tot += pes['idade']
    if pes['sexo'] == 'F':
        mul.append(pes['nome'])
    mult.append(pes.copy())
    pes.clear()
    cont = str(input('Deseja adicionar mais alguem? [S/N]')).upper()
    if cont == 'N':
        break
med = tot/len(mult)
for n, p in enumerate(mult):
    if p['idade'] > med:
        maior.append(p['nome'])
print(f'{len(mult)} pessoas cadastradas')
print(f'{med} é a média das idades')
print(f'Mulheres\n{mul}')
print((f'Idade maior que a média:\n{maior}'))
