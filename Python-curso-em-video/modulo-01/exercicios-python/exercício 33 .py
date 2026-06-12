#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = int(input('Digite o 3 números inteiros:'))
n2 = int(input(' '))
n3 = int(input(' '))

nMaior = n1
nMenor = n1

if (n2 > nMaior):
    nMaior = n2

if (n3 > nMaior):
    nMaior = n3

if (n2 < nMenor):
    nMenor = n2

if (n3 < nMenor):
    nMenor = n3
    

print(f'O número maior entre os 3 é: {nMaior} e o menor:{nMenor}')