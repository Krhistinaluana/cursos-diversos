#Faça um progrema que leia um número inteiro e diga se ele é ou não um número primo.

n = int(input('Digite um número para saber se é primo? '))

primo = True

if (n <= 1): 
    primo = False

for c in range(2, n):
    if (n % c ==0):
        primo =False

if primo == True: 
    print(f'O número {n} é primo.')
else:
    print(f'O número {n} não é primo')