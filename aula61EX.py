# Validar CPF 
import os

print('Bem vindo ao validador de CPF!')

while True:
    cpf_inserido = input('\nInsira um CPF (apenas digitos): ')\
        .replace(' ','')\
        .replace('-','')\
        .replace('.','')
# Validando o valor inserido
    try:
        cpf_numerico = int(cpf_inserido)
    except ValueError:
        print('informe apenas valores numericos')
        continue
    cpf_sequncial = cpf_inserido == cpf_inserido[1] * len(cpf_inserido)
    if cpf_sequncial:
        print('CPF sequancial')
        continue
# Verificando se possui a quantidade de digitos (max(11))
    cpf_avalidado = cpf_inserido.zfill(11)
    if len(cpf_avalidado) != 11:
        print('Valor insedrido fora do parão!\nMáximo de 11 digitos por CPF.')
        continue
# Formatando CPF
    cpf_impresso = ''
    for i in cpf_avalidado:
        cpf_impresso += i
        if len(cpf_impresso) == 3:
            cpf_impresso += '.'
        elif len(cpf_impresso) == 7:
            cpf_impresso += '.'
        elif len(cpf_impresso) == 11:
            cpf_impresso += '-'
#calculo primeiro numero
    nove_digitos = cpf_avalidado[:9]
    contagem_regressiva = 10
    resultado = 0
    for i in nove_digitos:
        resultado += int(i)*contagem_regressiva
        contagem_regressiva -= 1
    digito_1 = ((resultado*10)%11) if ((resultado*10)%11) <= 9 else 0
#validando primeiro digito
    if digito_1 != int(cpf_avalidado[9]):
        print(f'O CPF {cpf_impresso} é INVALIDO!')
        continue
#calculo segundo numero
    dez_digitos = cpf_avalidado[:10]
    contagem_regressiva = 11
    resultado = 0
    for i in dez_digitos:
        resultado += int(i)*contagem_regressiva
        contagem_regressiva -= 1
    digito_2 = ((resultado*10)%11) if ((resultado*10)%11) <= 9 else 0
#validando segundo digito
    if digito_2 != int(cpf_avalidado[10]):
        print(f'O CPF {cpf_impresso} é INVALIDO!')
        continue
    else:
        print(f'O CPF {cpf_impresso} é VALIDO!')