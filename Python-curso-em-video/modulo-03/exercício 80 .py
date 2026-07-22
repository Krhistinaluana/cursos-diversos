#Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.


guardarNum = []

for i in range (0,5):
    num = (int(input('Digite um valor: ')))
    posicao = 0
    while posicao < len(guardarNum) and num > guardarNum[posicao]:
         posicao += 1 
    guardarNum.insert(posicao, num)
    print(f'O número {num} foi inserido na {posicao}º posição ')
print(f'Todos os números digitados em ordem foram: {guardarNum}')