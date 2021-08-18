n1 = float(input('Insira a primeira nota: '))
n2 = float(input('Insira a segunda nota: '))
media = (n1 + n2)/2
if media < 5:
    print(f'Reprovado! Nota {media}')
elif media >= 5 and media < 6.9:
    print(f'Recuperaçao! Nota {media} :c')
else:
    print(f'Aprovado!! Nota: {media:.1f}')