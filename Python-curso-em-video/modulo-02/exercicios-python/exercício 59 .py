#Crie um programa que leia dois valores e mostre um menu na tela: [1] somas; [2]multiplicar; [3] maior; [4]novos números; [5] sair do programa. Seu programa deverá realizar a operação solicitada em cada caso. 

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
escolha = 0 

while escolha != 5:
    escolha = int(input('[1]Soma:\n[2]Multiplicar:\n[3]Maior:\n[4]Novos números:\n[5]Sair do programa:\nQual a sua escolha: '))
    if escolha == 1:
        equacao = n1 + n2
        print('=-','RESULTADO','=-')
        print(f'{n1} + {n2} = {equacao}')
        print('...'*5)
    if escolha == 2:
        equacao = n1 * n2
        print('=-','RESULTADO','=-')
        print(f'{n1} x {n2} = {equacao}')
        print('...'*5)
    if escolha == 3:
        if n1 > n2:
            maior = n1
            print('=-','RESULTADO','=-')
            print(f'{n1} é o maior.')
            print('...'*5)
        else:
            print('=-','RESULTADO','=-')
            print(f'{n2} é o maior.')
            print('...'*5)
    if escolha == 4:
            print('=-','RESULTADO','=-')
            print('Digite novos valor: ')
            n1 = int(input('Digite o primeiro valor: '))
            n2 = int(input('Digite o segundo valor: '))
            print('...'*5)
        
