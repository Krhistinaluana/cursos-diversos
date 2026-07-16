#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso crie duas listas extras que vão conter apenas os valores pares e o valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.


gNum = []
gNumPares = []
gNumImpares = []

while True:
    num = int(input('Digite um número: '))
    gNum.append(num)
    if num % 2 == 0:
        gNumPares.append(num)
    else:
        gNumImpares.append(num)
    condicao = str(input('Quer continuar [S/N]? ')) .upper() .strip()
    if condicao == 'N':
        break

print(f'Todos os números digitados foram: {gNum}\nOs números pares são: {gNumPares}\nOs números Ímpares são: {gNumImpares}')