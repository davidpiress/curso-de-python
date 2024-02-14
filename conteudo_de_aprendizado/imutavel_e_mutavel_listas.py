"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""

lista = [1, 2, 3, 4]  # temos uma lista dentro a variavel lista
lista[0] = 10         # de acordo com indice eu coloco o valor 10
listab = lista.copy() # jogo esse lista para uma variavel chamada listab com copy()
                      # no caso estou copiando a variavel
listab[3] = 1000      # agora para ter certeza que estou copiando com copy vou jogar o valor 1000 
                      # para o indice 3
print(lista)          # printa a lista
print(listab)         # depois a lista copiando que qesta dentro da listab