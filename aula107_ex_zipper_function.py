# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas listas na ordem.
# Use todos os valores da menor lista.

list_citys = ['Salvador', 'Ubatuba', 'Belo Horizonte']
list_states = ['BA', 'SP', 'MG', 'RJ']
list_complete = []
# while True:
#     if len(list_states) < len(list_citys):
#         for index_state, states in enumerate(list_states):
#             for index_city, citys in enumerate(list_citys):
#                 list_complet += (citys, states)
def verification_tuple_in_list(*args,**kwargs):
    def func_tuples(city,state):
        if city not in zipper(args) and state not in zipper(args):
            return func_tuples

@verification_tuple_in_list
def zipper(city,satate):
    list_complete += (city,satate)
    return zipper

zipper_list = zipper()
# for index_state, states in enumerate(list_states):
#     for index_city, citys in enumerate(list_citys):
#         if states not in list_complete and citys not in list_complete:
#             list_complete += (citys,states)

print(list_complete)