#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

soma = 0
for c in range (1,7):
    n = int(input(f'Digite o {c}º número? '))
    if (n % 2 == 0) :
        soma = soma + n

print(f'O resultado da soma dos pares são: {soma}')