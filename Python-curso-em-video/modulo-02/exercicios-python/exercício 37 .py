#Escreva um origrama que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: -1 para binário; -2 para octal e -3 para hexadecimal (bases numéricas)

numero = int(input('Digite um número: '))
base_Conv = int(input('Escolha qual será a base de conversão: \n1 - BINÁRIO\n2 - OCTAL\n3 - HEXADECIMAL\nRESPOSTA: '))

escolha = numero
if base_Conv == 1:
    escolha = bin(numero)
elif base_Conv ==2:
    escolha = oct(numero)
else:
    escolha = hex(numero)

print(f'O número {numero} convertido ficará {escolha}')