exp = str(input('Digite uma expressão: '))
pilha =[]
for c in exp:
    if c == '(':
        pilha.append('(')
    if c == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão é válida')
else:
    print('Sua expressão é inválida')