#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre: A)qual é o total gasto na compra; B)quantos produtos custam mais de R$1000.00; C)qual é o nome do produtos mais barato.

total = 0
produtoMil = 0
precoMenor = float('inf')
nomeBarato = ' '
while True:
    nome = str(input('Qual é o nome do produto? '))
    preco = float(input('QUal é o preço do produto? '))
    total = total + preco
    

    if preco > 1000:
        produtoMil = produtoMil + 1 
    if preco < precoMenor:
        precoMenor = preco
        nomeBarato = nome 
    print('=='*15)
    continuar = str(input(' Você quer continuar? S/N : ')) .upper() [0]
    print('=='*15)
    if continuar == 'N':
        break

print(f'O total gasto foi: R${total:.2f}\nProdutos acima de R$1000,00: {produtoMil}\nO produto mais barato é:{nomeBarato}')