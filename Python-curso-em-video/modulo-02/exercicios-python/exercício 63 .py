#Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequência de fibonacci. EX: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8.

nP = int(input('Quantos termos você quer mostrar?  '))

n1 = 0
n2 = 1
soma = 0
contador = 0

while contador != nP:
     print (f' {n1} ', end=' -> ')
     soma = n1 + n2
     n1 = n2
     n2 = soma
     contador +=1