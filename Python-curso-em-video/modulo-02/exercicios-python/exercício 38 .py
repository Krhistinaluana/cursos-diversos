#Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem.. O primeiro valor é maior; o segundo valor é maior; não existe valor maior, os dois são iguais. (Dar uma das respostas )

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

maior = n1
if (n2<n1):
    print('O primeiro valor é maior.')
elif (n2>n1):
    print('O segundo valor é maior.')
else:
    print('Não existe valor maior, os dois são iguais.')