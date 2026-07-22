#Crie um programa que tenha uma tupla com várias palabras (não usar acentos).Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('APRENDER', 'PROGRAMAS', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')

letrasProcuradas = 'A', 'E', 'I', 'O', 'U'

for cont in palavras:
    vogaisEncontradas = ''
    for letra in cont:
        if letra in letrasProcuradas:
            vogaisEncontradas = vogaisEncontradas + letra + ' '
    print(f'Na palavras {cont} temos {vogaisEncontradas} ')