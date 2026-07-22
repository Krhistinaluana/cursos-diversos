#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente. 


alunosN1N2 = [[], [], [], []]
while True:
    nome = str(input('Digite o nome do aluno: '))
    alunosN1N2[0].append(nome)
    N1 = int(input('Digite a 1º nota: '))
    alunosN1N2[1].append(N1)
    N2 = int(input('Digite a 2º nota: '))
    alunosN1N2[2].append(N2)
    media = (N1 + N2) / 2
    alunosN1N2[3].append(media)

    condicao = str(input('Quer continuar? [S/N]')) .upper() .strip()

    if condicao == 'N':
        break

print('-='*20)
print(f'{"Nº":<5}{"Nome":<20}{"Média"}')
print('-'*35)

for i in range(len(alunosN1N2[0])):
    print(i, alunosN1N2[0][i], alunosN1N2[3][i])

while True:
    aluno = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if aluno == 999:
        break
    if aluno < len(alunosN1N2[0]):
        print(f'Notas de {alunosN1N2[0][aluno]}: ')
        print(f'1º nota: {alunosN1N2[2][aluno]}: ')
        print(f'2º nota: {alunosN1N2[2][aluno]}: ')
    else:
        print('Aluno inexistente.')