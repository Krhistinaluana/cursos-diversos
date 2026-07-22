#O mesmo professor do desagio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada


import random

a1 = input('Nome do 1º aluno:')
a2 = input('Nome do 2º aluno:')
a3 = input('Nome do 3º aluno:')
a4 = input('Nome do 4ª aluno:')

alunos = [a1, a2, a3, a4]
random.shuffle(alunos)

print(f'A ordem de apresentação do trabalho será {alunos}')