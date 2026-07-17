#Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta. 

expressao = input('Digite uma expressão matemática: ')

pilha = []
sucesso = True

for caractere in expressao:
    if caractere == '(':
        pilha.append('(')

    elif caractere == ')':
        if len(pilha) == 0:
            sucesso = False
            break
        else:
            pilha.pop() 
if sucesso and len(pilha) == 0:
    print('Dua expressão está correta!')
else:
    print('Sua expressão está errada')