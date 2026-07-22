#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.


import random


tuplaNumerosAleatorios = ( random.randint(1,100),  random.randint(1,100),  random.randint(1,100),  random.randint(1,100),  random.randint(1,100) )
print(f'Os números gerados são: {tuplaNumerosAleatorios}')

print(f'O maior valor é: {max(tuplaNumerosAleatorios)}')
print(f'O menor valor é: {min(tuplaNumerosAleatorios)}')