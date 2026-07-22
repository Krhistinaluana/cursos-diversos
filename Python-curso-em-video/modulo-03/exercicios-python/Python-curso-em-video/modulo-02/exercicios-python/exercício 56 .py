#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: A média de idade do grupo; Qual é o nome do homem mais velho; Quantas mulheres tem menos de 21 anos 

idadeHomem = 0
nomeHomem = ' '
soma = 0
mulherMenoridade = 0
for c in range (0,4):
    nome = input('Digite seu nome: ')
    idade = int(input('Qual a sua idade: '))
    soma = soma + idade
    sexo = input('QUal seu sexo? [Masculino] ou [Feminino] ')
    sexo = sexo.upper()
    if idade > idadeHomem and sexo == 'MASCULINO':
            idadeHomem = idade
            nomeHomem = nome
    if idade < 21 and sexo == 'FEMININO':
        mulherMenoridade = mulherMenoridade + 1

media = soma / 4 

print(f'A média de idade do grupo é {media:.0f} anos, o nome do homem mais velho é: {nomeHomem} e temos {mulherMenoridade} mulheres menores que 21 anos.')