"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora_digitada = input("Informe a hora: ")

BOM_DIA = range(0,11)
BOA_TARDE = range(12,17)
BOA_NOITE = range(18,23)

try:
    hora = int(hora_digitada)
    if hora in BOM_DIA:
        print("Bom dia!")
    elif hora in BOA_TARDE:
        print("Boa tarde!")
    elif hora in BOA_NOITE:
        print("Boa noite!")
    else:
        print("O valor informado não esta no intervalo de 0 a 23 horas")
except:
    print("Valor informado não é um numero")