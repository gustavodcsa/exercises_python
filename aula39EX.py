''' Calculadora com while'''

while True:
    numero_1 = input('Informe um numero: ')
    if numero_1.isnumeric() is False:               # checa se o valor é numero
        print('Valor informado não é numerico, favor informar um numero')
        sair = input('Quer sair? [s]im: ').lower().startswith('s')
        if sair is True:
            break
        else:
            continue
    else:
        numero_1 = float(numero_1)

                                                    # primeiro valor inserido com sucesso
        
    operacao = input('Informe a operação desejada: [+] [-] [*] [/]: ')
    if operacao not in ('+','-','*','/'):           # verifica se a operção informada é valida
        print('Operção invalida')                            
        sair = input('Quer sair? [s]im: ').lower().startswith('s')
        if sair is True:
            break
        else:
            continue
                                                    # operação inserida com sucesso
    numero_2 = input('Informe um numero: ')
    if numero_2.isnumeric() is False:               # verifica se o segundo valor informada é valida
        print('Valor informado não é numerico, favor informar um numero')
        numero_1 = ''
        sair = input('Quer sair? [s]im: ').lower().startswith('s')
        if sair is True:
            break
        else:
            continue
    else:
        numero_2 = float(numero_2)
                                                    # segundo valor inserido com sucesso
    if operacao == '+':
        resultado = numero_1 + numero_2
    elif operacao == '-':
        resultado = numero_1 - numero_2
    elif operacao == '*':
        resultado = numero_1 * numero_2
    elif operacao == '/':
        resultado = numero_1 / numero_2
    
    print(f'{numero_1} {operacao} {numero_2} = {resultado}')
    
    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    
    if sair is True:
        break
