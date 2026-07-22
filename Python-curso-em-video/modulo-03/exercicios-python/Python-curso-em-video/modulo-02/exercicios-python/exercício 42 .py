#Refaça o desafio 35 doa triângulos, acrescentrando o recurso de mostrar que tipo de triângulo será formado: equilátero: todos os lados iguais; isósceles: dois lados iguais; escaleno: todos os lados diferentes.

print('--'*15)
print('   Analisador de triângulos')
print('--'*15)
reta1 = float(input('Primeiro segmento:'))
reta2 = float(input('Segundo segmento: '))
reta3 = float(input('Terceiro segmento: '))

if (reta1+reta2) > reta3 and (reta1+reta3) > reta2 and (reta2+reta3) > reta1:
    print('É possível formar um triângulo: ', end='')
    if (reta1 == reta2 == reta3):
        print('Equilátero!')
    elif (reta1 == reta2 != reta3) or (reta1 == reta3 != reta2) or (reta2 == reta3 != reta1):
        print('Isósceles!')
    else:
        print('Escaleno!')
else:
    print('Não é possível formar um triângulo.')