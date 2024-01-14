# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears

import os
import sys
import json
print('---------- Bem vindo a sua lista de tarefas 📝 -------------')

list_everything = []
list_remake = []

def validate_option(option):
    if option:
        if option in ('LISTAR', 'DESFAZER', 'REFAZER','SAIR'):
            return option
        else:
            os.system('cls')
            print('Opção invalida    ⚠️ ')
    else:
        os.system('cls')
        print('🚫 Por favor, informe uma opção  🚫')

def return_option(option,iten = None):
    if option == 'LISTAR':
        os.system('cls')
        iten = input('\n✍🏾 Informe a inclusão: ')
        item_include = iten 
        list_everything.append(item_include)
    
    elif option == 'DESFAZER':
        if list_everything == []:
            os.system('cls')
            print('Nenhum item para ser removido    ⚠️ ')
        else:
            list_remake.append(list_everything.pop()) 
    
    elif option == 'REFAZER':
        if list_remake == []:
            os.system('cls')
            print('Nenhum item para ser reposto    ⚠️')
        else:
            list_everything.append(list_remake.pop())
    
    elif option == 'SAIR':
        os.system('cls')
        with open('C:\\Users\\gusta\\Downloads\\list_everything.json','w+',encoding='utf8') as file:
            json.dump(
                list_everything,
                file,
                ensure_ascii=False,
                indent=2,
            )
        print('💾 Lista de tarefas salva')
        sys.exit()

while True:
    selected_option = validate_option(
        input('Opções:\n🖊️    Listar\n↩️    Desfazer\n🔄️   Refazer\n❌   Sair\nSelecione uma opção: ').upper().strip()
    )

    return_option(selected_option)
    print('\n📝 Lista:')
    print(*list_everything,sep='\n')

