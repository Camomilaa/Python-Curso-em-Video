prec = float(input('Qual o preço do produto? '))
desc = prec*0.05
print('Seu novo preço, agora com 5% de desconto, equivale a R${:.2f}'.format(prec - desc))