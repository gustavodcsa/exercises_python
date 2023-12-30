import random
# Gerando primiro nove digitos
nove_digitos = ''
for digito in range(9):
    nove_digitos += str(random.randint(0,9))

# Gerando 10 digito
contador_regressivo_1 = 10
resultado_1 = 0
for i in nove_digitos:
    resultado_1 += (int(i)*contador_regressivo_1)
    contador_regressivo_1 -= 1

decimo_digito = ((resultado_1*10)%11) if ((resultado_1*10)%11) <= 9 else 0

# inserindo 10 digito
dez_digitos = nove_digitos + str(decimo_digito)

# Gerando 11 digito
contador_regressivo_2 = 11
resultado_2 = 0
for i in dez_digitos:
    resultado_2 += (int(i)*contador_regressivo_2)
    contador_regressivo_2 -= 1

decimo_primeiro_digito = ((resultado_2*10)%11) if ((resultado_2*10)%11) <= 9 else 0

# inserindo 11 digito
cpf = dez_digitos + str(decimo_primeiro_digito)

# Mostrando cpf formado 
cpf_impresso = ''
for i in cpf:
    cpf_impresso += i
    if len(cpf_impresso) == 3:
        cpf_impresso += '.'
    elif len(cpf_impresso) == 7:
        cpf_impresso += '.'
    elif len(cpf_impresso) == 11:
        cpf_impresso += '-'
print(cpf_impresso)

