# filter é um filtro funcional
def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]


filter_produtos = [
    p for p in produtos
    if p['preco'] > 22
]

funcao_filter = filter(
    lambda p: p['preco'] > 105,
    produtos
)

print_iter(funcao_filter)
print_iter(filter_produtos)



def filtra_preco(produto):
    if produto['preco'] > 105:
        return produto

funcao_filter = filter(
    filtra_preco,
    produtos
)

print_iter(funcao_filter)