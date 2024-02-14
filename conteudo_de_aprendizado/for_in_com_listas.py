"""
for in com listas
"""
lista = ['Maria', 'Helena', 'Luiz']
i = 0
for nomes in lista:
    i += 1
    print(i, nomes)

for nome in 'davi', 'maria':
    i += 1
    print(i, nome)
print()
    
indice = range(len(lista))

for i in indice:
    print(i, lista[i])