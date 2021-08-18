top20 = ('Palmeiras', 'Atlético-MG', 'Bragantino', 'Fortaleza', 'Flamengo', 'Athletico-PR',
         'Ceará SC', 'Santos', 'Atlético-GO', 'Bahia', 'Corinthians', 'Fluminense', 'Juventude',
         'Sport Recife', 'Internacional', 'Cuiabá', 'São Paulo', 'América-MG', 'Grêmio', 'Chapecoense')

print(f'{top20[:5]} são os 5 primeiros colocados')
print(f'{top20[16:]} são os 4 últimos colocados')
print(f'A seguir os times em ordem alfabética:\n{sorted(top20)}')
print(f'A chapecoense está na {top20.index("Chapecoense") + 1}º posição')