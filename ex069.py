maior = hom = mn = 0
while True:
    id = int(input('Qual sua idade? '))
    sex = str(input('Qual seu sexo? [F/M]')).upper()

    if sex == 'F' or sex == 'M':
        if id > 18:
            maior += 1
        if sex == 'M':
            hom += 1
        if sex == 'F' and id < 20:
            mn += 1
        cont = str(input('Deseja continuar? [S/N] ')).upper()
        if cont == 'N':
            break

print(f'{maior} maiores de 18 anos\n{hom} homens\n{mn} mulheres com menos de 20 anos')