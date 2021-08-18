from datetime import datetime
infos = dict()
infos['nome'] = str(input('Nome: '))
ano = int(input('Ano de nascimento: '))
infos['idade'] = datetime.now().year - ano
infos['ctps'] = int(input('Carteira de trabalho: (0 caso n tenha): '))
if infos['ctps'] != 0:
    infos['contratacao'] = int(input('Ano de contratação: '))
    infos['salario'] = float(input('Salário: '))
    infos['aposentadoria'] = infos['idade'] + ((infos['contratacao'] + 35) - datetime.now().year)
print(infos)
for k,v in infos.items():
    print(f'{k}: {v}')