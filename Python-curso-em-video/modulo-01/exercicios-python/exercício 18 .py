#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo

import math

a = float(input('Digite um ângulo:'))
rad = math.radians(a)
print(f'O seno do ângulo {a}º é {math.sin(rad):.2f}, seu cosseno é {math.cos(rad):.2f} e a tangente {math.tan(rad):.2f}') 