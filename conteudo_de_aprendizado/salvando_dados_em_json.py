import json

pessoa = {
    'nome': 'davi queiroz 2',
    'sobrenome': 'Miranda',
    'enderecos': [
        {'rua': 'R1', 'numero': 32},
        {'rua': 'R2', 'numero': 55},
    ],
    'altura': 1.8,
    'numeros_preferidos': (2, 4, 6, 8, 10),
    'dev': True,
    'nada': None,
}

# Escrita com "w" e transform em json
with open('aula.json', 'w') as arquivo:
    json.dump(pessoa, arquivo, ensure_ascii=False, indent=2)


# leitura com "r" e transform em python novamente
with open('aula.json', 'r') as arquivo:
    pessoa = json.load(arquivo)
    print(pessoa)
