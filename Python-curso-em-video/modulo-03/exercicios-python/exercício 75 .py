#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre: A)Quantas vezes apareceu o valor 9; B)Em que posição foi digitado o primeiro valor 3. C)Quais foram os números pares. 

tuplaValores = (int(input('Digite o 1ºvalor: ',)), int(input('Digite o 2ºvalor: ')), int(input('Digite o 3ºvalor: ')), int(input('Digite o 4ºvalor: ')))

print(f'Você digitou os valores {tuplaValores}')
print(f'O número 9 apareceu {tuplaValores.count(9)}X')
if 3 in tuplaValores:
    print(f'O valor 3 foi digitado na posição {tuplaValores.index(3)+1}')
else:
    print('O valor 3 não foi digitado em nenhuma posição')


print('Os numeros pares são: ')
for cont in tuplaValores:
    if cont % 2 == 0:
       print(cont)