#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido. (sem utilizar listas)


import random

a1 = input('Nome do 1º aluno:')
a2 = input('Nome do 2º aluno:')
a3 = input('Nome do 3º aluno:')
a4 = input('Nome do 4ª aluno:')

print(f'O alun(o) sorteado foi: {random.choice([a1, a2, a3, a4])}')