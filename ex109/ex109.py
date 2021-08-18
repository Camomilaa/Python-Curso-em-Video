import moeda
m = int(input('Digite o valor: R$'))
c = str(input('Deseja formatar? ')).upper()
if c == 'S':
    moeda.aumentar(m, c=True)
    moeda.diminuir(m, c=True)
    moeda.metade(m, c=True)
    moeda.dobro(m, c=True)
else:
    moeda.aumentar(m)
    moeda.diminuir(m)
    moeda.metade(m)
    moeda.dobro(m)