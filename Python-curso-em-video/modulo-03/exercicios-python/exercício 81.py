#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:  A)Quantos números foram digitados; B)A lista de valores, ordenada de forma descrecente; C) Se o valor 5 foi digitado e está ou não na lista.

guardarNum = []
guardaNum5 = ' '

while True:
    num = int(input('Digite um número: '))
    guardarNum.append(num)
    if 5 in guardarNum:
        guardaNum5 = 'FOI'
    else:
        guardaNum5 = 'NÃO FOI'
    condicao = str(input('Quer continuar [S/N]? ')) .upper() .strip()
    if condicao == 'N':
        break

guardarNum.sort(reverse=True)
print(f'Foram digitados: {len(guardarNum)} elementos\nA lista ordenada de forma descrecente fica: {guardarNum}\nO valo [5] {guardaNum5} digitado.') 