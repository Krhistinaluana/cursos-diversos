#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = int(input('Digite o 1º valor: '))
n2 = int(input('Digite o 2º valor '))
n3 = int(input('Digite o 3º valor: '))

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
    

print(f'O maior valor é: {nMaior} e o menor:{nMenor}')