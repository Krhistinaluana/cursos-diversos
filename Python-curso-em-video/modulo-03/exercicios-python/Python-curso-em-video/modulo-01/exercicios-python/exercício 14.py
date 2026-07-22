#Escreva um programa que converta uma temperatura digitada em °C para °F

tc = float(input('Informe a temperatura em °C:'))
tf = (tc * 1.8) + 32

print(f'A temperatura de {tc:.1f}°C corresponde a {tf:.1f}°F!')
