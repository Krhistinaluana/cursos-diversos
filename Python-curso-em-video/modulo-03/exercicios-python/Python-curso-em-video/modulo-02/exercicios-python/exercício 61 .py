#Refaça o desafio 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

print('-='*12)
print(' PROGRESSÃO ARITMÉTICA')
print('-='*12)

i = int(input('Qual será o número inicial da sequência: '))
r = int(input('Qual será a razão da progressão? '))
contador = 0

while contador <= 10:
    termo = i + (contador*r)
    contador += 1
    print(termo, end= ' -> ')
print('FIM')