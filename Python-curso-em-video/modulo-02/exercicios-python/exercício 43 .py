#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mos: ABAIXO QUE 18.5: abaixo do peso; entre 18.5 e 25: peso ideal; 25 até 30:sobrepeso; 30 até 40: obesidade; acima de 40: obesidade mórbida.

print('=='*10)
print(' CALCULANDO SEU IMC')
print('=='*10)
peso = float(input('Digite seu peso: (kg) '))
altura = float(input('Digite sua altura: (m) '))

imc = peso / (altura**2)
print(f'Seu imc é: {imc:.1f}')
if (imc < 18.5):
    print('Você está ABAIXO DO PESO')
elif (imc < 25):
    print('Você está no seu PESO IDEAL')
elif (imc < 30):
    print('Você está com SOBREPESO')
elif (imc < 40):
    print('Você está com OBESIDADE')
else:
    print('Você está com OBESIDADE MÓBIDA')