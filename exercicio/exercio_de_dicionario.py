# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
import copy
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]
print('preço aumentado em 10%')
preco_aumentado = [{'nome': produto['nome'], 'preco': round(produto['preco'] * 1.1, 2)}
                   for produto in produtos]
print(*preco_aumentado, sep='\n')
print()
print('copia')
copia_profunda = copy.deepcopy(preco_aumentado)
print(*copia_profunda, sep='\n')
print()
print('nome em descrecente')
# Ordene os produtos por nome decrescente (do maior para menor)
decrescente = sorted(produtos, key=lambda produtos: produtos['nome'], reverse=True)
print(*decrescente, sep='\n')
print()
print('copia')
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
produtos_ordenados_por_nome = copy.deepcopy(decrescente)
print(*produtos_ordenados_por_nome, sep='\n')
print()
print('crescente dos preço')
# Ordene os produtos por preco crescente (do menor para maior)
preco_crescente = sorted(produtos, key=lambda produtos: produtos['preco'])
print(*preco_crescente, sep='\n')
print()
print('copia')
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
produtos_ordenados_por_preco = copy.deepcopy(preco_crescente)
print(*produtos_ordenados_por_preco, sep='\n')