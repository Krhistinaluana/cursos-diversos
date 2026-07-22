#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele 

algo = input('Digite algo: ')
print('O tipo primitivo desse valor é', type (algo))

print('Só tem espaço ?', algo.isspace()) 
print('É um número?', algo.isalnum())
print('É alfabético?', algo.isalpha())
print('Está em maiúscula?', algo.isupper())
print('Está em minúscula?', algo.islower())
print('Está capitalizada?', algo.istitle())