def multiplicar(*args):
    total = 1
    for n in args:
        total *= n
    return total


multiplicação = multiplicar(10, 2, 3, 4, 5)
print(multiplicação)

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def even_or_odd(x):
    if x%2 == 0:
        return f'{x} is Even'
    else:
        return f'{x} is Odd'
    
value_x = input('Enter an integer value: ')
try:
    value_x = int(value_x)
    print(even_or_odd(value_x))
except ValueError:
    print('Value entered is not integer!')