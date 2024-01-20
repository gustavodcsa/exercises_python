import json
from aula127_ex_class_json_a import file_json, Time

with open(file_json, 'r', encoding='utf-8') as file:
    times = json.load(file)

internacinal = Time(nome = 'Internacinal', estado = 'Rio Grande do Sul', estadio = 'Beira Rio', torcida = '2 milhões', cores = ['Vermelho', 'Branco'])

print(internacinal.descricao())