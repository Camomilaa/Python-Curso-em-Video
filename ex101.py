from datetime import datetime
def voto(ano):
    atual = datetime.now().year
    idade = atual - ano
    if idade < 16:
        return f'NEGADO'
    elif idade >= 16 and idade < 18:
        return f'OPCIONAL'
    else:
        return f'OBRIGATÓRIO'

nsc = int(input('Em que ano você nasceu? '))
print(f'SEU VOTO É {voto(nsc)}')