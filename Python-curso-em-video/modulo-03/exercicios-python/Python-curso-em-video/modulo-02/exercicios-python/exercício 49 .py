#Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

n_Tab = int(input('Qual tabuada deseja visualizar? '))

for c in range(0, 11):
    resul = c * n_Tab
    print(f'{n_Tab} x {c} = {resul}')