casa = float(input('Qual o valor da casa que deseja financiar? '))
sal = float(input('Qual o valor do seu sálario? '))
ano = int(input('Em quantos anos deseja pagar? '))
lim = sal * 0.3
mes = ano * 12
par = casa / mes

if par > lim:
    print(f'Emprestimo negado! Seu limite mensal é de {lim:.2f}, e você tentou pagar {par:.2f}')
    print('Tente aumentar a quantidade de anos!')
else:
    print('Emprestimo realizado com sucesso')