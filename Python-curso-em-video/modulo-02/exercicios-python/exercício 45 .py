#Crie um programa que faça o computador jogar jokenpô com você (pedra, papel e tesoura )

import random

print('=='*10)
print('   JOGO POKÉMON')
print('=='*10)

lista = ['pedra', 'papel', 'tesoura'] 
computador = random.choice(lista)

participante = int(input('Qual sua opção:\n1 - Pedra \n2 - Papel \n3 - Tesoura \nReposta:'))

if (computador == 'pedra') and (participante == 1):
    print(f'A escolha do computador: {computador} e do participante: {participante}: EMPATE')
elif (computador == 'pedra') and (participante == 2):
    print(f'A escolha do computador: {computador} e do participante: {participante}: PARTICIPANTE GANHOU!')
elif (computador == 'pedra') and (participante == 3):
    print(f'A escolha do computador: {computador} e do participante: {participante}: COMPUTADOR GANHOU')
elif (computador == 'papel') and (participante == 1):
    print(f'A escolha do computador: {computador} e do participante: {participante}: COMPUTADOR GANHOU')
elif (computador == 'papel') and (participante == 2):
    print(f'A escolha do computador: {computador} e do participante: {participante}: EMPATE')
elif (computador == 'papel') and (participante == 3):
    print(f'A escolha do computador: {computador} e do participante: {participante}: PARTICIPANTE GANHOU')
elif (computador == 'tesoura') and (participante == 1):
    print(f'A escolha do computador: {computador} e do participante: {participante}: PARTICIPANTE GANHOU')
elif (computador == 'tesoura') and (participante == 2):
    print(f'A escolha do computador: {computador} e do participante: {participante}: COMPUTADOR GANHOU')
elif (computador == 'tesoura') and (participante == 3):
    print(f'A escolha do computador: {computador} e do participante: {participante}: EMPATE')
