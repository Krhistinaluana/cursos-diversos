#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.


maiorP = 0
menorP = float('inf')
for c in range(1,6):
    peso = int(input(f'Digite o peso da {c}º pessoa (kg): '))
    if peso > maiorP:
        maiorP = peso
    if peso < menorP:
        menorP = peso

print(f'O maior peso é de {maiorP}Kg e o menor peso é {menorP}Kg')