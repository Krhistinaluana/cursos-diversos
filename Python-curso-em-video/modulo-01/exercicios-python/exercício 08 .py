#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

m = float(input('Quantos metros você quer converter?'))
c = m*100
ml = m*1000

print(f'O valor de {m}m corresponde a {c:.0f}cm e {ml:.0f}ml')