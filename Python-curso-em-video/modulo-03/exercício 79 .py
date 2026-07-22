#Crie um programa onde o usuário possa digitar váios valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

guardaNum = []

while True:
    num = int(input('Digite um número: '))
    if num not in guardaNum:
        guardaNum.append(num)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado!Não vou adicionar...')
    resposta = str(input('Quer continuar? [S/N] ')) .upper() .strip()
    if resposta == 'N':
        break

print('-='*30)
guardaNum.sort( )
print(f'Todos os valores digitados foram: {guardaNum}')

