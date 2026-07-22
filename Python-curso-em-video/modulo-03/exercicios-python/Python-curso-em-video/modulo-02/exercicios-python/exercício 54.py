#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores. (considere maioridade 21 anos)


from datetime import date
maiorI = 0
menorI = 0
ano_Atual = date.today().year


for c in range (1,8):
    ano_Nasc = int(input(f'Qual O ano de nascimento DA {c}º pessoa? EX: (XXXX) '))
    if (abs(ano_Atual - ano_Nasc) < 21):
        menorI = menorI + 1
    else:
          maiorI = maiorI + 1

print(f'{maiorI} Pessoas atingiram a maioridade')
print(f'{menorI} Pessoas não atingiram a maioridade')
