#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre: A)quantas pessoas tem mais de 18 anos; B)quantos homens foram cadastrados; C)quantas mulheres tem menos de 20 anos.


mulher = 0
homem = 0
maiorIdade = 0 
while True:
    idade = int(input('Qual é sua idade? '))
    sexo = str(input('Qual é o seu sexo? [F/M] ')) .strip() .upper() [0]
    if idade > 18:
       maiorIdade = maiorIdade + 1
    if sexo == 'F' and idade < 20:
        mulher = mulher + 1
    if sexo == 'M':
        homem = homem + 1
    print('='*20)
    continuar = str(input(' Quer continuar? ')) .strip() .upper() [0]
    print('='*20)
    if continuar == 'N':
     break

print(f'Foram cadastrados {maiorIdade} pessoas maiores que 18 anos\nHomens:{homem}\nMulheres com menos de 20 anos: {mulher}' )