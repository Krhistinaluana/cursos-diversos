#Melhore o jogo DESAFIO 028 onde o computador vai 'pensar' em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

import random
n = random. randint(0,10)
print('...'*20)
print('Vou sortear um número entre 0 e 10: tente adivinhar ..')
print('...'*20)
tentativa = int(input('Tente descobrir qual número foi sorteado? '))
palpite = 1

while tentativa != n: 
   tentativa = int(input('Haaaá não, você errou, tentei novamente? '))
   palpite = palpite + 1

print(f'Parabéns, você acertou! foram necessários {palpite} palpites até o número correto')
