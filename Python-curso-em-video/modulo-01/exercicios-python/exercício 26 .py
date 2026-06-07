#Faça um programa que leia uma frase pelo teclado e mostre: Quantas vezes aparece a letra "A"; Em que posição ela aparece a primeira vez: Em que posição ela aparece a última vez

frase = input('Digite uma frase:')
quantA = frase.count('a')
primeiroA = frase.find('a') 
ultimoA = frase.rfind('a') 

print(f'A letra A aparecem o total de {quantA} vezes \nA letra A aparece a primeira vez na {primeiroA + 1}º posição\nA letra A aparece na última vez {ultimoA + 1}º posição')