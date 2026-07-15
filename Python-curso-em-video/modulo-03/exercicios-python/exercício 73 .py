#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre: A)Apenas os 5 priemiros colocados; B)Os últimos 4 colocados da tabela; C)Uma lista com os times em ordem alfabética; D)Em que posição na tabela está o time da champecoense.

selecaoBrasileira = ('Palmeiras', 'Flamengo', 'Fluminense', 'Athletico-PR', 'Bragantino', 'Bahia', 'Coritiba', 'São Paulo', 'Atlético-MG', 'Corinthians', 'Cruzeiro', 'Botafogo', 'EC Vitória', 'Internacional', 'Santos', 'Grêmio', 'Vasco da Gama', 'Remo', 'Mirassol', 'Chapecoense')

print('-='*15)
print(f'Lista de times da Sleção Brasileira {selecaoBrasileira}')
print('-='*15)
print(f'Os 5 primeiros colocados na Seleção Brasileira foram:{selecaoBrasileira[0:5]}')
print('-='*15)
print(f'\nOs últimos 4 colocados da tabela foram:\n{selecaoBrasileira[-4:]}\n')
print('-='*15)
print(f'Todos os times da Seleção Brasileira em ordem alfabética:\n {sorted(selecaoBrasileira[1:])}')
print('-='*15)
print(f'\nO time champecoense esta na posição {selecaoBrasileira.index("Chapecoense")}º')
