
#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e monstre quanto dólares ela pode comprar (considere US$1,0 = $3,27)

r = float(input('Quanto dinheiro você tem na carteira? R$'))

c = r / 5.04

print(f'Com R${r:.2f} você pode comprar US${c:.2f}')