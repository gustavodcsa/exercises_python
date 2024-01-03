def criar_multiplicador(multiplicador):
    def valor(valor_x):
        return f'{multiplicador}X{valor_x}: {valor_x * multiplicador}'
    return valor

valor = int(input('Informe o valor inicial: '))
max_multiplicador = int(input('Informe o valor máximo a ser multiplicado: '))

valor_final = criar_multiplicador(valor)

for i in range(1, max_multiplicador + 1):
    print(valor_final(i))
