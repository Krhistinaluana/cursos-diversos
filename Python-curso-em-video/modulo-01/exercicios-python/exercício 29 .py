#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado; A multa vai custar R$7.00 por cada km acima do limite.

velocidade = float(input('Qual a velocidade que o carro de encontra?'))

if (velocidade > 80) :
    multa = (velocidade - 80) * 7
    print(f'Você foi multado e o valor da multa  sera R$ {multa:.2f}')
else:
    print('Parabéns, você esta dentro da velocidade recomendada.')

