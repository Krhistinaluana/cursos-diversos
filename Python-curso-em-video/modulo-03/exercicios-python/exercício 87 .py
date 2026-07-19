#Aprimore o desafio anterior, mostrando no final: A) A soma de todos os valores pares digitados. B) A soma dos valores da terceira coluna. C)O maior valor da segunda linha. 

matriz = [[], [],[]]
somaValores = 0
somaColunaB = 0

for linha in range(3):
    for coluna in range(3):
        valor = int(input(f'Digite o valor [{linha}][{coluna}]: '))
        matriz[linha].append(valor)
        if valor % 2 == 0:
            somaValores = somaValores + valor
        if coluna == 2:
            somaColunaB = somaColunaB + matriz[linha][coluna]


print(matriz[0])
print(matriz[1])
print(matriz[2])
print('-='*10)
print(f'A soma de todos os valores pares digitados são: {somaValores}')
print(f'A soma dos valores da terceira coluna são: {somaColunaB}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')