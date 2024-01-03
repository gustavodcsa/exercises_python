'''
Exercico
exiba os indices a lista
0 Maria
1 Helena 
2 Luiz
'''
lista = ['Maria','Helena','Luiz']
indices = range(len(lista))
for indece in indices:
    print(indece, lista[indece], type(lista[indece]))