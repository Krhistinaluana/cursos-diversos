  #Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.


guardarLista = []
for i in range (0,5):
  n = int(input('Digite um valor: '))
  guardarLista.append(n)

print(f'O maior valor é {max(guardarLista)}')
print(f'O menor valor é {min(guardarLista)}')
