"""
Exercício
Crie uma função que encontra o primeiro duplicado considerando o segundo
número como a duplicação. Retorne a duplicação considerada.
Requisitos:
    A ordem do número duplicado é considerada a partir da segunda
    ocorrência do número, ou seja, o número duplicado em si.
    Exemplo:
        [1, 2, 3, ->3<-, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
        [1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)
        [1, 4, 9, 8, ->9<-, 4, 8] (retorne 9)
    Se não encontrar duplicados na lista, retorne -1
"""
lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]

def listas(lista):
    def numero_lista(numero):
        return lista[numero]
    return numero_lista

lista = listas(lista_de_listas_de_inteiros)
lista_verificacao = []

duplicado = False
valor_duplicado = None
indice_duplicado = None

for indice, lista in enumerate(lista_de_listas_de_inteiros):
    lista_numero = lista

    for indice_valor, valor_numero in enumerate(lista):
        if duplicado == False:
            if valor_numero in lista_verificacao:
                duplicado = True
                valor_duplicado = valor_numero 
                indice_duplicado = indice_valor
            else:
                indice_duplicado = -1
        lista_verificacao.append(valor_numero)
    
    if duplicado:
        print(f'Lista {indice+1}) {lista_numero} -> Possui valor {valor_duplicado} duplicado no indece {indice_duplicado}\n')
    else:
        print(f'Lista {indice+1}) {lista_numero} -> Não possui valor duplicado {indice_duplicado}\n')
    
    lista_verificacao = []
    duplicado = False
    valor_duplicado = None
    indice_duplicado = None


        