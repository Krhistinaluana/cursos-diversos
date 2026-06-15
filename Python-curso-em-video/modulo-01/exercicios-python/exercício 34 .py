#Escreva um programa que pergunte o salário de um funcionário e calculo o valor do seu aumento. Para salários superiores a R$1250.00, calculo um aumento de 10%. Para os inferiores ou iguais , o aumento é de 15%.

salario = float(input('Qual é o seu salário: '))

if (salario <= 1250):
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)


print(f'Seu salário de R$ {salario:.2f} passa a ser R$ {novo:.2f}')

    