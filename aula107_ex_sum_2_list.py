"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]
"""
list_a = [10, 2, 3, 40, 5, 6, 7]
list_b = [1, 2, 3, 4]

def zipper(list_1, list_2):
    interval = min(len(list_1),len(list_2))
    return [list_1[i]+list_2[i] for i in range(interval)]

print(zipper(list_a,list_b))

