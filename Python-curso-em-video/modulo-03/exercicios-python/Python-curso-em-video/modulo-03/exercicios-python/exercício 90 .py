#Faça um programa que leia o nome e média de um aluno, guardando também a situação em um dicionário. No final mostre o conteúdo da estrutura na tela 


situacaoAlunos = {}

nomeAluno = input("Nome: ")
mediaAluno = float(input("Média: "))

situacaoAlunos['NomeAluno'] = nomeAluno
situacaoAlunos['mediaAluno'] = mediaAluno

if mediaAluno >= 7:
    situacaoAlunos['situacao'] = 'Aprovado'
elif mediaAluno >= 5 and mediaAluno < 7:
    situacaoAlunos['situacao'] = 'Em recuperação'
else:
    situacaoAlunos['situacao'] = 'Reprovado'

print('-='*20)
print(f'- Nome é igual: {situacaoAlunos["NomeAluno"]}')
print(f'- Média é igual: {situacaoAlunos["mediaAluno"]}')
print(f'- A situação é igual: {situacaoAlunos["situacao"]}')

