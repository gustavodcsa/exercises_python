import sys

primeiro_valor = input('Digite um valor: ')
if primeiro_valor.isnumeric():
    primeiro_valor_int = int(primeiro_valor)
else:
    print('Valor invalido! Deve-se informar um numero inteiro')
    sys.exit()

segundo_valor = input('Digite outro valor: ')
if segundo_valor.isnumeric():
    segundo_valor_int = int(primeiro_valor)
else:
    print('Valor invalido! Deve-se informar um numero inteiro')
    sys.exit()

if primeiro_valor >= segundo_valor:
    print(
        f'{primeiro_valor=} é maior ou igual '
        f'ao que {segundo_valor=}'
    )
else:
    print(
        f'{segundo_valor=} é maior '
        f'do que {primeiro_valor=}'
    )