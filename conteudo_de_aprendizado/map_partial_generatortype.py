# map, partial, GeneratorType e esgotamento de Iterators

from functools import partial
from types import GeneratorType


# map - para mapear dados
def desenpacotando(iterador):
    print(*list(iterador), sep='\n')
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]
def aumentando_preco(valor, porcentagen):
    return round(valor * porcentagen, 2)

aumenta_dez_porcento = partial(
    aumentando_preco,
    porcentagen=1.1
)


aumenta_preco = [
    {**p, 'preco': aumenta_dez_porcento(p['preco'])}
    for p in produtos
]


desenpacotando(aumenta_preco)
print()

def funcao_aumenta(produto):
    return {**produto,
            'preco': aumenta_dez_porcento(produto['preco'])}

mepeando_preco = map(
    funcao_aumenta,
    produtos
)
desenpacotando(mepeando_preco)








