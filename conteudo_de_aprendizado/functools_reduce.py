# reduce - faz a redução de um iterável em um valor
from functools import reduce

produtos = [
    {'nome': 'Produto 5', 'preco': 10},
    {'nome': 'Produto 1', 'preco': 22},
    {'nome': 'Produto 3', 'preco': 2},
    {'nome': 'Produto 2', 'preco': 6},
    {'nome': 'Produto 4', 'preco': 4},
]

# pode ser consideraso um acumalor somando a acumalor com o novo valor
ruduces = reduce(
    lambda ac, p: ac + p['preco'],
    produtos,
    0
)

# Essa forma vocẽ tambem gera um acumulador com for
total = 0
for p in produtos:
    total += p['preco']

print(ruduces)
print(total)