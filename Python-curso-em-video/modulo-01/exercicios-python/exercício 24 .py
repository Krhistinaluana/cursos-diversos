#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

cidade = input('Digite o nome de uma cidade?')
verificacao = cidade[0:5] == 'Santo'

print(verificacao)

