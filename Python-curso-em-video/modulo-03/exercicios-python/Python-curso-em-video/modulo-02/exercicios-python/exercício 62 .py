#Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.

print('-='*12)
print(' PROGRESSÃO ARITMÉTICA')
print('-='*12)

i = int(input('Qual será o número inicial da sequência: '))
r = int(input('Qual será a razão da progressão? '))

termos = 1
contador = 1
posicao = 0 
while termos != 0: 
    termos = int(input('\nQuantos termos vamos mostrar?'))
    if termos >0:
        for contador in range(0,termos):
            termoP= i + (posicao*r)
            print(termoP, end=' -> ')
            posicao += 1