import json
from aula127_ex_class_json_a import file_json

with open(file_json, 'r', encoding='utf-8') as file:
    dados_class = json.load(file)

class Time:
    def __init__(self, **kwargs):
        for dado in dados_class.keys():
            setattr(self, dado, kwargs.get(dado, None))

palmeiras = Time(nome = 'Palmeiras', estado = 'São Paulo', estadio = 'Alians Park', torcida = '5 milhões', cores = ['Verde', 'Branco'])

print(palmeiras.__dict__,sep='\n')