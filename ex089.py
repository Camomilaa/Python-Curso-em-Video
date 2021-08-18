al = []
sal = []
c = num = 0
while True:
    al.append(str(input('Insira o nome do aluno: ')))
    al.append(float(input('Insira nota 1: ')))
    al.append(float(input('Insira nota 2: ')))
    al.append(c)
    c += 1

    sal.append(al[:])
    al.clear()
    cont = str(input('Deseja adicionar mais? [S/N] ')).upper()
    if cont == 'N':
        break

for a in sal:
    tot = a[1] + a[2]
    print(f'{a[3]}. Média de alune {a[0]}: {tot / 2}')

while True:
    ver = int(input('Digite o número do aluno, do lado esquerdo do seu nome para saber mais sobre ele: '))
    if sal[ver][3] == ver:
        print(f'{sal[ver][3]}. Nome: {sal[ver][0]}\nNota 1: {sal[ver][1]}\nNota 2: {sal[ver][2]}')
    else:
        break
