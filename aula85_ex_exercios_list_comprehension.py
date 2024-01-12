# Crie uma lista com os números pares de 1 a 10.
lista = [
    valor for valor in range(10)
            if valor%2 == 0
]

print(f'{lista}\n')

# Crie uma lista com os quadrados dos números de 1 a 10.
lista = [
    valor**2 for valor in range(10)
]

print(f'{lista}\n')

# Dada uma lista de palavras, crie uma nova lista contendo o tamanho de cada palavra.
lista = ['ANA', 'MAGNOLIA', 'ERIKA', 'MARIA', 'VANESSA', 'BARBARA']

lista_nova = [
    (len(palavara), palavara) 
    for palavara in lista
]

print(f'{lista_nova}\n')

# Dada uma lista de números, crie uma nova lista apenas com os números maiores que 5.
lista = [0,10,2,36,54,98,8,6,51,5,9,554,5]

lista_nova = [
    maior_que_5 for maior_que_5 in lista
    if maior_que_5 > 5
]

print(f'{lista_nova}\n')

# Crie uma lista com as letras maiúsculas de uma string.
frase = 'A desvalorização do mundo humano aumenta em proporção direta com a valorização do mundo das coisas.'.title()

lista_maiusculas = [
    letra_maiuscula 
    for letra_maiuscula in frase
    if letra_maiuscula == letra_maiuscula.upper() and letra_maiuscula != ' '
]

print(f'{frase}\n{lista_maiusculas}\n')

# 6-Dada uma lista de números, crie uma nova lista contendo apenas os números pares e maiores que 10.
lista = [0,10,2,36,54,98,8,6,51,5,9,554,5]

lista_nova = [
    par_maior_que_10 for par_maior_que_10 in lista
    if par_maior_que_10 > 5 and par_maior_que_10%2 == 0
]

print(f'{lista_nova}\n')

# 7-Dada uma lista de nomes, crie uma nova lista apenas com os nomes que começam com a letra "A".
lista = ['ANA', 'MAGNOLIA', 'ERIKA', 'MARIA', 'VANESSA', 'BARBARA']

lista_nova = [
    palavara
    for palavara in lista
    if palavara.lower().startswith('a')
]

print(f'{lista_nova}\n')

# 8-Dada uma lista de frutas, crie uma nova lista com o comprimento de cada fruta, apenas para as frutas com mais de 5 letras.
lista = ['BANANA', 'MANGA', 'UVA', 'LARANJA', 'TANGERINA', 'MAÇÃ']

lista_nova = [
    (len(fruta), fruta) 
    for fruta in lista
    if len(fruta) > 5
]

print(f'{lista_nova}\n')

# 9-Dada uma lista de números, crie uma nova lista com o dobro de cada número, mas apenas se o número for ímpar
lista = [0,10,2,36,54,98,8,6,51,5,9,554,5]

lista_nova = [
    dobro_dos_impares*2 for dobro_dos_impares in lista
    if dobro_dos_impares%2 != 0
]
print(lista)
print(f'{lista_nova}\n')