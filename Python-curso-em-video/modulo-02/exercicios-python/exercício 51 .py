#Desenvolva um programa que leia o primeiro termo e a razão de uma Progressão Aritmética. No final mostre os 10 primeiros termos dessa progressão.

print('-='*12)
print(' PROGRESSÃO ARITMÉTICA')
print('-='*12)

i = int(input(' Qual será o número inicial da sequência: '))
r = int(input('Qual será a razão da progressão? '))

for c in range(0, 10):
    termo = i + (c*r)
    print(termo)
