# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
import json
CAMINHO_ARQUIVO = 'aula127.json'

class Pessoa:
    def __init__(self, idade, nome):
        self.nome = nome 
        self.idade = idade




p1 = Pessoa('joão', 23)
p2 = Pessoa('maria', 23)
p3 = Pessoa('joana', 23)
bd = [vars(p1), vars(p2), vars(p3)]

with open(CAMINHO_ARQUIVO, "w") as arquivo:
    json.dump(bd, arquivo, ensure_ascii=False, indent=2)