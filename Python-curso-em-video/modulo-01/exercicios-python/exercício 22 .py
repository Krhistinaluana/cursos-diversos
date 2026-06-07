#Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúscula; O nome com todas as letras minúsculas; Quantas letras tem ao todo (sem considerar espaços): Quantas letras tem o primeiro nome

nome = input('Qual seu nome?')
textoSemEspaco = len(nome) - nome.count(' ')
Pnome = nome.split()[0]

print(f'Seu nome com todas as letras maiúscula fica: {nome.upper()}')
print(f'Seu nome com todas as letras minúscula fica: {nome.lower()}')
print(f'Seu nome tem o total de {textoSemEspaco} letras (sem considerar os espaços)')
print(f'O seu primeiro nome possui {len(Pnome)}')