#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal sabendo que ela nao pode exceder 30% do salário ou então o empréstimo será negado.

print('Seja bem -vindo')
valorEmp = float(input('Qual o valor do empréstimo? '))
salario = float(input('Qual o salário do contratante? '))
anos = int(input('Quantos anos deseja pagar o empréstimo? '))

mensal = (anos*12)
prestacao = valorEmp / mensal

if prestacao <= (salario*30 / 100):
    print(f'Parabéns seu empréstimo foi aprovado, suas parcelas ficaram em {mensal} x de R$ {prestacao:.2f}')
else:
    print('Empréstimo negado, você não atende as especifícações necessárias para liberação.')