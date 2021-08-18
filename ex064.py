n = 0
somN = 0
conN = 0
while n != 999:
    n = int(input('Digite um número '))
    if n != 999:
        somN += n
        conN += 1
print(f'A soma dos números equivale a {somN}\nForam {conN} números digitados')