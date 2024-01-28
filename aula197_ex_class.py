# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, valor):
        self._motor = valor

    @property
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor

    def detalhe_carro(self):
        return f'O carro {self.nome} é fabricado por {self._fabricante}'\
            f' e possui o motor {self._motor}'


class Motor:
    def __init__(self, nome):
        self.nome = nome
        self._carros = []

    def inserir_carro(self, carro):
        self._carros.append(carro)

    def mostrar_carros(self):
        return f'O motor {self.nome} esta presente nos seguintes carros {self._carros}'


class Fabricante:
    def __init__(self, nome):
        self.nome = nome
        self._carros = []
        self._motores = []

    def mostrar_carros(self):
        return f'A fabricante {self.nome} possui os seguintes carros {self._carros}'

    def inserir_carros(self, nome):
        self._carros.append(nome)


uno = Carro('Uno')
basico = Motor('Basico')
fiat = Fabricante('Fiat')

uno.motor = basico.nome
uno.fabricante = fiat.nome

basico.inserir_carro(uno.nome)
fiat.inserir_carros(uno.nome)

print(basico.mostrar_carros())
print()
print(fiat.mostrar_carros())
print()
print(uno.detalhe_carro())
