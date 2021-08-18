prec = float(input('Indique o preço do produto: '))
print('Condições de pagamento:\n1. À vista dinheiro/cheque: \n2. Á vista no cartão:')
print('3. Em até 2x no cartão: \n4. 3x ou mais no cartão:')
selec = int(input('Selecione: '))
if selec == 1:
    nprec =  prec - (prec * 0.1)
    print(f'Valor: R${nprec:.2f}')
elif selec == 2:
    nprec = prec - (prec * 0.05)
    print(f'Valor: R${nprec:.2f}')
elif selec == 3:
    p = int(input('Quantas vezes? '))
    print(f'Valor: R${prec:.2f}')
    parc = prec / p
    print(f'parcelas de R${parc:.2f} em {p} vezes')
elif selec == 4:
    nprec = prec + (prec * 0.2)
    p = int(input('Quantas vezes? '))
    print(f'Valor: R${nprec:.2f}')
    parc = nprec / p
    print(f'parcelas de R${parc:.2f} em {p} vezes')
else:
    print('Erro!')