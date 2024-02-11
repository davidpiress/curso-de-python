# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

a = ['BA', 'SP', 'MG', 'RJ']
b = ['Salvador', 'Ubatuba', 'Belo Horizonte']

def zipper(l1, l2):                                    #criado dois parametros para a variavel "a e b"
    intervalo = min(len(l1), len(l2))                  # usando função min com lista com os menores indices
    return [(l1[i], l2[i]) for i in range(intervalo)]  # retornando uma list compreenshion eterando a cada volta
print(zipper(a, b))                                    # reconhecendo os parametros

# a função abaixo chamada "zip" ja faz tudo com o proprio python
print(list(zip(a, b)))