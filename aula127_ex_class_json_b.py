import json
from aula127_ex_class_json_a import file_json

with open(file_json, 'r', encoding='utf-8') as file:
    dados_class = json.load(file)


class Time:
    def __init__(self, **kwargs):
        for dado in dados_class.keys():
            setattr(self, dado, kwargs.get(dado, None))
            setattr(self.__class__, dado, property(
                self.getter(dado), self.setter(dado)))

    def getter(self, name):
        def get(self):
            return getattr(self, name)
        return get

    def setter(self, name):
        def set(self, value):
            setattr(self, name, value)
        return set


palmeiras = Time(nome='Palmeiras', estado='São Paulo',
                 estadio='Alians Park', torcida='5 milhões', cores=['Verde', 'Branco'])


print(palmeiras.__dict__)
