#Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print('BEM VINDO AO CAIXA 24HR')
print('-='*20)

valorSacado = int(input('Qual valor será sacado? '))

notas50 = valorSacado // 50
resto50 = valorSacado % 50
notas20 = resto50  // 20
resto20 = resto50 % 20 
notas10 = resto20 // 10
resto10 = resto20 % 10
notas1 = resto10 // 1 
resto1 = resto10 % 1 

print (f'O valor sacado será {valorSacado}, correpondente à {notas50} notas de R$50, {notas20} notas de R$20, {notas10} notas de R$10 e {notas1} notas de R$1.')