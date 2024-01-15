# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears

import os, sys, json
print('---------- Bem vindo a sua lista de tarefas📝 -------------')

def validate_option(option):
    if option:
        if option in ('INSERIR', 'DESFAZER', 'REFAZER','SAIR', 'LISTA'):
            return option
        else:
            print('Opção invalida ⚠️\n')
    else:
        print('🚫 Por favor, informe uma opção 🚫\n')

def include_option(iten = None):
    iten = input('\n✍🏾 Informe a tarefa: ')
    if iten is not None and iten is not '':
        list_everything.append(iten)
        print(f'Item {iten} incluso com sucesso ✅\n')
    else:
        print('Nenhum item informado ⚠️\n')
    
def remove_option():
    if list_everything == []:
        print('Nenhum item para ser removido ⚠️ \n')
    else:
        list_remake.append(list_everything.pop()) 
        print(f'Item {list_remake[-1]} removido com sucesso ✅\n')
    
def remake_option():
    if list_remake == []:
        print('Nenhum item para ser reposto ⚠️\n')
    else:
        list_everything.append(list_remake.pop())
        print(f'Item {list_everything[-1]} reposto com sucesso ✅\n')
    
def exit_option():
    with open('C:\\Users\\gusta\\Downloads\\list_everything.json','w',encoding='utf8') as file:
        json.dump(
            list_everything,
            file,
            ensure_ascii=False,
            indent=2,
        )
    print("LISTA:",*list_everything, sep='\n')
    print('\n💾 Lista de tarefas salva\n')
    sys.exit()

def filer_list():
    try:
        with open('C:\\Users\\gusta\\Downloads\\list_everything.json','r',encoding='utf8') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

list_everything = filer_list()
list_remake = []

while True:
    selected_option = validate_option(
        input('\nOpções:\n🖊️    Inserir\n↩️    Desfazer\n🔄️   Refazer\n\
🗒️    Lista\n❌   Sair\nSelecione uma opção: ').upper().strip()
    )   
    comandos = {
        "INSERIR": lambda: include_option(),
        "DESFAZER": lambda: remove_option(),
        "REFAZER": lambda: remake_option(),
        "SAIR": lambda: exit_option(),
        "CLEAR": lambda: os.system('clear'),
        "LISTA": lambda: print("LISTA:",*list_everything, sep='\n')
    }
    comando = (comandos.get(selected_option) if comandos.get(selected_option) is not None else comandos["LISTA"])
    comando()