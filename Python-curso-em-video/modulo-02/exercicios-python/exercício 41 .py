#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade: até 9 anos: mirim; até 14 anos: infantil; até 19 anos: junior; até 20 anos: sênior; acima: master.

from datetime import date

ano_Nasc = int(input('Para descobrir qual é a sua categoria, digite o ano em que você nasceu?'))

ano_Atual = date.today().year
idade = abs(ano_Nasc - ano_Atual)

print(f'O atleta tem {idade} anos.')

if idade <= 9:
    print('Categoria: MIRIM')
elif idade <= 14:
    print('Categoria: INFANTIL')
elif idade <= 19:
    print('Categoria: JUNIOR')
elif idade <= 25:
    print('Categoria: SÊNIOR')
else:
    print('Categoria: MASTER')
