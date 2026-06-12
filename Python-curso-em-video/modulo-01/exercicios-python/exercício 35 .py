#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se eles podem ou não formar um triângulo.

reta1 = int(input('Digite o comprimento de três retas:'))
reta2 = int(input(''))
reta3 = int(input(''))

if (reta1+reta2) > reta3 and (reta1+reta3) > reta2 and (reta2+reta3) > reta1:
    print('É possível formar um triângulo')
else:
    print('Não é possível formar um triângulo.')