#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa. #Usando módulos

import math
c1 = float(input('Qual o valor do primeiro cateto?'))
c2 = float(input('Qual o valor do segundo cateto?'))

r = math.sqrt(c1**2 + c2**2)

print(f' O comprimento da hipotenusa será {r:.2f}')