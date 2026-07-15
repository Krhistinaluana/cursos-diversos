#Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

import random
print('='*20)
print(' Jogo PAR ou ÍMPAR')
print('='*20)

vitoriaJogador = 0
vitoriaPc = 0
escolha = ' '
while True:
    escolha = str(input('Par ou Ímpar? ')) .strip() .upper() [0]
    n = int(input('Digite sua jogada? '))

    numeroPc = random.randint(1,10)
    print(f'Você jogou {n} e o computador {numeroPc}')

    soma = n + numeroPc
    if soma % 2 == 0 and escolha == 'P':
        vitoriaJogador = vitoriaJogador + 1
    elif soma % 2 ==1 and escolha == 'Í':   
        vitoriaJogador = vitoriaJogador +1
    else:
        vitoriaPc = vitoriaPc + 1
        break

print(f'O jogador computou o total de {vitoriaJogador} vitórias')