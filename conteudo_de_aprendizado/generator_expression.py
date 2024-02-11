"""
    Com o generator expression pode usar para imprimir com o print
    que no caso do iterar com o for passar por todo as dados a ser
    ptintado com print
"""
from sys import getsizeof

# Esta pasando por todos os dados

lista = [n for n in range(10)]
print(lista)
print(getsizeof(lista))

"""
    Enquanto eu ainda não chamar uma o dado que esta na memoria vou ver so a numero de dado
    <generator object <genexpr> at 0x7f160d66e190>
"""
generator = (n for n in range(10))

# <generator object <genexpr> at 0x7f160d66e190>
print(generator)
print(getsizeof(generator))


# para ver cada dado dentro da generator expression devo usar o NEXT
print(next(generator))
print(next(generator))
print()
# Usando yield

def gen1():
    yield 1
    yield 2
    yield 3

def gen2():
    yield from gen1()
    yield 6
    yield 7
    yield 8
    yield 9

g = gen2()
for numeros in g:
    print(numeros)

print()


def min_max(n=0, maximo=10):
    while True:
       yield n
       n += 1
       if n > maximo:
            return n

g1 = min_max()
for numeros in g1:
    print(numeros)                                                              







