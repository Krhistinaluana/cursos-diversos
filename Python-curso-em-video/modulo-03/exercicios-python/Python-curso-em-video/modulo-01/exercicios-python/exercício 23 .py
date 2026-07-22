#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados. Ex: Digite um número: 1834 
#Unidade: 4; Dezena: 3; Centena:8; Milhar: 1 

n = int(input('Digite um número entre 0 até 9999 (sem decimais): '))

unidade = n % 10
dezena = (n // 10) % 10
centena = (n//100) % 10
milhar = (n//1000) % 10

print(f'Unidade: {unidade}\nDezena: {dezena}\nCentena: {centena}\nMilhar: {milhar}')
