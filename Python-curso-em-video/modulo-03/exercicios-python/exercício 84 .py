#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final mostre: A)Quantas pessoas foram cadastradas; B)Uma listagem com as pessoas mais pesadas; C)Uma listagem com as pessoas mais leves.

pessoas = []
pesos = []
while True:
    nome = input('Digite o nome: ')
    peso = int(input('Digite o peso: '))
    pessoas.append((nome, peso))
    condicao = str(input('Deseja continuar [S/N]: ')) .upper() .strip()
    if condicao == 'N':
        break

for p in pessoas:
        pesos.append(p[1])
maiorPeso = max(pesos)
menorPeso = min(pesos)

quantidade = len(pessoas)
print(f'Foram cadastradas {quantidade} pessoas')
pessoaPesada = '' #Usando string
pessoaLeve = [ ] #Usando lista (acumulando) p. treino
for p in pessoas:
     if p[1] == maiorPeso:
          pessoaPesada = pessoaPesada + p[0] + ', '
print(f'As pessoas mais pesadas são: {pessoaPesada}')
for p in pessoas:
     if p[1] == menorPeso:
            pessoaLeve.append(p[0])
print(f'As pessoas mais leves são: {pessoaLeve}...')