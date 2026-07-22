#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou nao continuar a digitar valores.


contador = 0
soma = 0
continuar = True 
maior = 0
menor = float('inf')
while continuar != 'N':
    n =int(input('Digite um número: '))
    soma += n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    continuar = str(input('Deseja continuar [S] ou [N]? ')) .upper() .upper() [0]
    contador += 1

media = soma / contador 
print(f'A média dos valores digitado foi {media:.2f}, o maior valor digitado {maior} e o menor {menor}')
