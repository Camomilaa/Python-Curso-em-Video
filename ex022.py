nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome com todas as letras maiúsculas: {}'.format(nome.upper()))
print('Seu nome com todas as letras minúsculas: {}'.format(nome.lower()))
print('A quantidade de letras total é igual a {}'.format(len(nome) - nome.count(' ')))
esp = nome.find(' ')
print('A quantidade de letras no seu primeiro nome é igua a {}'.format(esp))