#Faça um progema que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.


while True:
    n_Tab = int(input('Qual tabuada deseja saber: '))
    if n_Tab < 0:
        break
    for c in range (0,11):
        result = c * n_Tab
        print(f'{n_Tab} X {c} = {result}')
print('Não calculamos números negativos..')