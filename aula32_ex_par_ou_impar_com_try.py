"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero_digitado = input("Digite um número interio: ")

try:
    numero_inteiro = int(numero_digitado)
    if (numero_inteiro%2) == 0:
        print('O número é par')
    else:
        print('O número é impar')
except:
    print('O valor digitado não é interio')
