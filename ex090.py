alu = dict()
alu['Nome'] = str(input('Digite o nome: '))
alu['Média'] = float(input('Digite a média do aluno: '))
for k, v in alu.items():
    print(f'{k}: {v}')
if alu['Média'] < 6:
    print(f'{alu["Nome"]} está de recuperação!')
else:
    print(f'{alu["Nome"]} passou!')