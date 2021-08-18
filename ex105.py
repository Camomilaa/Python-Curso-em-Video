def notas(*num, sit = False):
    n = dict()
    n['Quantidade'] = len(num)
    n['Maior'] = max(num)
    n['Menor'] = min(num)
    n['Media'] = sum(num)/len(num)
    if sit == True:
        if n['Media'] > 6:
            n['Situação'] = 'Aprovade'
        else:
            n['Situação'] = 'Reprovade'

    print(n)

notas(6.5, 7.2, 3.6, sit = True)