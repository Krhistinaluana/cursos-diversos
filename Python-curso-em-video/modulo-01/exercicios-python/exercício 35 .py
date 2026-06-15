#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se eles podem ou não formar um triângulo.
print('--'*15)
print('   Analisador de triângulos')
print('--'*15)
reta1 = float(input('Primeiro segmento:'))
reta2 = float(input('Segundo segmento: '))
reta3 = float(input('Terceiro segmento: '))

if (reta1+reta2) > reta3 and (reta1+reta3) > reta2 and (reta2+reta3) > reta1:
    print('É possível formar um triângulo')
else:
    print('Não é possível formar um triângulo.')