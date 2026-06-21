#Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.

print('A soma de número ímpares e que são múltiplos de 3 no intervalo de 0 - 500 é:')

soma = 0
for c in range(0,500):
    if (c % 3 == 0) and (c % 2 == 1):
        soma = soma + c
print(soma)