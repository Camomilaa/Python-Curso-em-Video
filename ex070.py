quant = caro = gas = 0
while True:
    nom = str(input('Nome do produto: '))
    val = float(input('Valor: '))

    quant += 1
    if quant == 1:
        it = nom
        itVal = val
    else:
        if val < itVal:
            itVal = val
            it = nom

    if val > 1000:
        caro += 1

    gas += val


    cont = str(input('Deseja continuar? [S/N] ')).upper()
    if cont == 'N':
        break
print(f'O total gasto na compra foi {gas:.2f}\n{caro} produtos custaram mais de R$1000\nO item mais barato foi {it} e seu valor foi {itVal:.2f}')