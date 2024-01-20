import json
file_json = 'dados_class.json'
class Time:
    def __init__(self, nome, estado, estadio, torcida, cores):
        self.nome = nome
        self.estado = estado
        self.estadio = estadio
        self.torcida = torcida
        self.cores = cores

    def descricao(self):
        cores_str = ', '.join(self.cores)
        return f'---------------------------------------------------------------------------------------------\n'\
               f'O time {self.nome}, é do Estado do {self.estado},\ntem como casa o estádio {self.estadio} e\n'\
               f'possui uma torcida de aproximadamente {self.torcida}.\nSuas cores principais são {cores_str}.\n'\
               f'---------------------------------------------------------------------------------------------\n'

if __name__ == '__main__':
    vasco = Time('Vasco', 'Rio de Janeiro', 'São Januário', '4,5 milhões', ['Branco', 'Preto', 'Vermelho'])

    print(vasco.descricao())

    with open(file_json,'w',encoding='utf-8') as file:
        dados = vasco.__dict__
        json.dump(
            vasco.__dict__,
            file,
            ensure_ascii=False,
            indent=2
        )
