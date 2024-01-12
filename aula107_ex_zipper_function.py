# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas listas na ordem.
# Use todos os valores da menor lista.

list_citys = ['Salvador', 'Ubatuba', 'Belo Horizonte']
list_states = ['BA', 'SP', 'MG', 'RJ']

def zipper(list_1, list_2):
    interval = min(len(list_1),len(list_2))
    return [(list_1[i],list_2[i]) for i in range(interval)]

print(zipper(list_citys,list_states))

from itertools import zip_longest
print(list(zip(list_citys,list_states)))
print(list(zip_longest(list_citys,list_states)))
