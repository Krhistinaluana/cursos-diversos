#Escreva um programa que faça o computador 'pensar' em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
#O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
n = random.randint(0,5)
print('...'*20)
print('Vou sortear um número entre 0 e 5: tente adivinhar..')
print('...'*20)
tentativa = int(input('Tente descobrir qual número foi sorteado? '))

if (tentativa == n):
    print('Parabéns, você acertou!')
else:
    print('Haaaá não, você errou.')