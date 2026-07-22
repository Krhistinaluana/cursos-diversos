#Faça um programa que leia a largura e a altura de uma parece em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m²

altura = float(input('Qual altura de sua parede?'))
largura = float(input('Qual largura de sua parede?'))

area = largura * altura
tinta = area / 2

print(f'\nA sua parede tem a dimensão de {largura} x {altura} e sua área é de {area}m²')
print(f'Para pintar essa parede, você precisará de {tinta}L de tinta.')