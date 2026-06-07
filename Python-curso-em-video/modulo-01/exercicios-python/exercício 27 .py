#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente. Ex: Ana Maria de Souza 
#Primeiro = Ana; Último = Souza

nome = input('Digite seu nome completo:')

Pnome = nome.split()[0]
Unome = nome.split()[-1]

print(f'Seu primeiro nome é: {Pnome} e seu último nome é: {Unome}')
