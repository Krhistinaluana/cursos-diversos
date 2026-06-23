#Faça um progrema que leia um número qualquer e mostre o seu fatorial. ex: 5! = 5x4x3x2x1 = 120#Crie um programa que leia dois valores e mostre um menu na tela: [1] somas; [2]multiplicar; [3] maior; [4]novos números; [5] sair do programa. Seu programa deverá realizar a operação solicitada em cada caso. 


n = int(input('Digite um número para calcular seu fatorial: '))
c = n
f = 1
print(f'Calculando {n}! = ', end=' ')
while c > 0:
    print(f'{c} ', end=' ')
    print(' X ' if c > 1 else ' = ', end=' ' )
    f *= c
    c -= 1
print(f'{f}')

