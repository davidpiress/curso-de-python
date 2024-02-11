"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]
"""
from itertools import zip_longest

lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

soma_lista = []

for i in range(len(lista_b)):
    soma_lista.append(lista_a[i] + lista_b[i])
print(soma_lista)

soma_lista1 = [x + y for x, y in zip_longest(lista_b, lista_a, fillvalue=0)]
print(soma_lista1)