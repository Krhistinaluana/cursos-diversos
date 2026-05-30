#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

s = float(input('Qual seu sálario?'))
ns = s + (s * 0.15)

print(f'\nO seu salário com 15% de aumento pasarrá ser:  R${ns:.2f}')