#Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira
##EX: Digite um número? 6.127, o número 6.127 tem a parte inteira 6.

import math
n = float(input('Digite um número com casas decimais:'))

print(f'O número {n} tem a parte inteira {math.trunc(n)}')