#Escreva um programa que pergunte o salário de um funcionário e calculo o valor do seu aumento. Para salários superiores a R$1250.00, calculo um aumento de 10%. Para os inferiores ou iguais , o aumento é de 15%.

salario = float(input('Qual é o seu salário:'))

if (salario <= 1250):
    percentual = 15
else:
    percentual = 10

aumentoSalario = (percentual * salario) / 100
salarioTotal = salario + aumentoSalario

print(f'Você terá um aumento de {percentual}% equivalente a R$ {aumentoSalario:.2f} totalizando, R$ {salarioTotal:.2f}')

    