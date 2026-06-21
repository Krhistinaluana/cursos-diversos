#Crie um programa que leia uma frase qualquer e diga se ela é palíndromo, desconsiderando os espaços. ex APOS A SOPA; A SACADA DA CASA; O LOBO AMA O BOLO 

frase = (input( 'Digite uma frase para saber se ela é palíndromo? '))

frase = frase.upper( )
frase = frase.replace(' ', '')

verificacao = False
controle = 0

for c in range(len(frase) -1, len(frase) //2, -1):
    controle = len(frase) -1 -c 
    if frase[c] != frase[controle]:
        verificacao = False
        break
    else:
        verificacao = True
        

if verificacao == True:
    print(f'A frase "{frase}" é um palíndromo')
else:
    print('Está frase não é um palíndromo.')
