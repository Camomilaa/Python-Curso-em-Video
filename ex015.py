km = float(input('Quantos km foram rodados pelo carro alugado? '))
dia = int(input('Quantos dias ele foi alugado? '))
dial = 60*dia
kml = km*0.15
print('Preço a pagar R${:.2f}'.format(dial+kml))