#Faça um programa que ajude um jogador da mega sena a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta. 

import random
import time 

jogos = int(input('Quantos jogos serão gerados? '))
megaSena = []

for c in range(jogos):
    jogo = []
    for n in range(6):
        jogo.append(random.randint(1,60))
    megaSena.append(jogo)

for c, j in enumerate(megaSena):
    print(f'Jogo {c+1}: {j}')
    time.sleep(1)