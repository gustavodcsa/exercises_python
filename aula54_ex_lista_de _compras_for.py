"""
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de 
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de indeices inecistntes na lista.

"""
import os 

lista_compras = []
print('Bem vindo a sua lista de compras!')
while True:

    print("\nInforme o que deseja fazer:")
    selecao = input("[I]nserir, [A]pagar, [L]istar, [S]air: ").lower().strip()
#Inclusão de intem
    if selecao == 'i':
        os.system('cls')
        item_inserido = input('Informe o intem a ser inserido: ').title().strip()
        if item_inserido in lista_compras:
            print('Item já esta na lista!')
            continue
        else:
            lista_compras.append(item_inserido)
            print(f'O item "{item_inserido}" foi inserido com sucesso!')
#Exclusão de item
    elif selecao == 'a':
        item_excluido = input('Infome o intem ou indece que deseja apagar: ').title().strip()
        if item_excluido.isdigit():
            item_excluido = int(item_excluido)
            try:
                if lista_compras[item_excluido] in lista_compras:
                    for i, n in enumerate(lista_compras):
                        if item_excluido == i:
                            lista_compras.pop(i)
                            os.system('cls')
                            print(f'O item "{item_excluido}" foi excluido com sucesso!')
            except:
                os.system('cls')
                print('Indice informado não consta na lista!')
        else:
            if item_excluido not in lista_compras:
                os.system('cls')
                print('Item informado não consta na lista!')
                continue
            else:
                for i, n in enumerate(lista_compras):
                    if item_excluido == n:
                        lista_compras.pop(i)
                        os.system('cls')
                        print(f'O item "{item_excluido}" foi excluido com sucesso!')
#Exibir lista de compras
    elif selecao == 'l':
        os.system('cls')
        if len(lista_compras) == 0:
            print('Lista vazia!')
        else:
            print('Lista de compras: \n')
            for i, n in enumerate(lista_compras):
                print(i, n)
#Sair da lista de compras
    elif selecao == 's':
        break
#Invalido                
    else:
        os.system('cls')
        print('Opção invalida')
        continue


