#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento: à vista dinheiro/cheque: 10% de desconto; à vista no cartão: 5% de desconto; em até 2x no cartão: preço normal; 3x ou mais no cartão: 20% de juros.

print ('=='*20)
print('     Vamos cálcular o seu desconto')
print('=='*20)

valorP = float(input('Qual o valor do produto R$: '))
forma_Pagamento = int(input('Escolha a forma de pagamento: \n1 - À vista (dinheiro/cheque)\n2 - À vista no cartão de crédito\n3 - Até 2x no cartão de crédito\n4 - 3x ou mais no cartão de crédito: '))

desconto = 0

if forma_Pagamento == 1:
    desconto = valorP - (valorP * 10 / 100)
    print(f'Seu produto terá 10% de desconto de R${valorP:.2f}, você pagará R${desconto:.2f}')
elif forma_Pagamento == 2:
    desconto = valorP - (valorP * 5 / 100)
    print(f'Seu produto terá 5% de desconto de R${valorP:.2f}, você pagará R${desconto:.2f}')
elif forma_Pagamento == 3:
    desconto = valorP
    print(f'Seu produto não terá desconto, você pagará R${valorP:.2f} em até 2x no cartão de crédito')
else:
    desconto = valorP + (valorP * 20 / 100)
    print(f'Para o parcelado para 3x ou mais você será cobrado com juros de 20% e seu produto passará ter o valor R${desconto:.2f}')