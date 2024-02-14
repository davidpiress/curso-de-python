"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete -> (CRUD)
Criar, ler, alterar, apagar = lista[i] 
"""


"""listas = ['maria', 'queiroz', 'pires']
print(listas[0], type(listas))"""

lista = [20, 30, 40, 50]
lista[1] = 1000
print(lista, type(lista))
print()

# Métodos úteis: 'append' add no final

lista1 = [20, 30, 40, 50]
lista1.append(5000)
print(lista1)
print()

# Métodos úteis: 'insert' e para ser utilizado 
# aonde dever ser mudado de acordo com o indice 

lista1 = [20, 30, 40, 50]
lista1.insert(3, 5000)
print(lista1)
print()

# Métodos úteis: 'extend' e para extender uma lista com a outra
lista = ['maria', 'joao', 'fernando']
lista1 = [20, 30, 40, 50]
lista1.extend(lista)
print(lista1)
print()

# Métodos úteis: 'pop' apaga o ultimo do final

lista1 = [20, 30, 40, 50]
lista1.pop()
print(lista1)
print()

# Métodos úteis: del apaga de acordo com indice escolhido 
# da lista

lista5 = [20, 30, 40, 50]
del lista5[0]
print(lista5)
print()

# Métodos úteis: 'clear' apaga tudo e deixa uma lista vazia

lista1 = [20, 30, 40, 50]
lista1.clear()
print(lista1)
print()

# Métodos úteis: '+' calcater lista com outras listas 
lista3 = 'josafa', 'nanda', 'vanessa'
lista4 = 1, 2, 3, 4, 5
print(list(lista3 + lista4))

