  #Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.


guardarLista = []
mai = 0
men = 0
for i in range (0,5):
  guardarLista.append(int(input(f'Digite um valor na posição {i}: ')))
  if i == 0:
      mai = men = guardarLista[i]
  else:
      if guardarLista[i] > mai:
          mai = guardarLista[i]
      if guardarLista[i] < men:
          men = guardarLista[i]


print('=-' * 20)
print(f'Você digitou os valores {guardarLista}')
print(f'O maior valor digitado foi {mai} nas posições ', end='')
for c, v in enumerate(guardarLista):
      if v == mai:
            print(f'{c}...', end ='')
print()
print(f'O menor valor digitado foi {men} nas posições ', end='')
for c, v in enumerate (guardarLista):
      if v == men:
        print(f'{c}...', end='')
print()
