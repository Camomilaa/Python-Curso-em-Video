alt = float(input('Qual a altura da sua parede? '))
lar = float(input('Qual a largura da sua parede? '))
m2 = alt * lar
print('Você necessita de {:.1f} litros de tinta'.format(m2/2))