#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

p = float(input('Qual o preço do produto?'))
vf = p - (p * 0.05)

print(f'\nO valor desse produto com desconto de 5% irá sair por: R${vf:.2f}')