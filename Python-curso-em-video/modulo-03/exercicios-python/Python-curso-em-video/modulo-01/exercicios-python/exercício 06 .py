#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

n = int(input('Digite um número:'))
d = n * 2
t = n * 3
rq = n ** (1/2)

print(f'O dobro do número {n} é {d}, o triplo é {t} e sua raiz quadrada é {rq:.2f}')