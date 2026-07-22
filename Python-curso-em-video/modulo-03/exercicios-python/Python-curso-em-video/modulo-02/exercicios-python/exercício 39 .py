#Faça um programa que leia o ano de nscimento de um jovem e informe, de acordo com sua idade: Se ele ainda vai se alistar ao serviço militar; se é a hora de se alistar ou se ja passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date 

print('--' * 7)
print(' ALISTAMENTO')
print('--' * 7)

nasc = int(input('Em que ano você nasceu? '))
ano_Atual = date.today().year
idade = abs(nasc - ano_Atual)

if (idade < 18) :
    print(f'Você possuí {idade} anos e ainda não vai se alistar ao serviço militar')
    print(f'Faltam {abs(idade - 18)} anos para você se alistar ')
elif (idade == 18):
    print('Parabéns, está na hora se alistar ao serviço militar.')
else:
    print('Infelizmente, já passou do prazo para se alistar.')
    print(f'Se passaram {idade - 18} anos de seu alistamento obrigatório.')
