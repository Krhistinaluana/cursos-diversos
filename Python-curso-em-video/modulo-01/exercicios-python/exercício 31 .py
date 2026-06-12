#Desenvolva um programa que pergunte a distância de uma viagem em KM. Calculo o preço da passagem, cobrando R$0.50 por Km para viagens de até 200Km e 0.45 para viagens mais longas.

distancia = float(input('Qual a distância da viagem em KM?'))

if (distancia <= 200):
    preco = distancia * 0.50
    print(f'O valor que você gastará de passagem será R$: {preco:.2f}')
else:
    preco = distancia * 0.45
    print(f'O valor que você gastará de passagem será R$: {preco:.2f}')