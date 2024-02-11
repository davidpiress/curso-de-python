# 🟢 Keyword-Only Arguments (*) - * sozinho ❗️NÃO SUGA❗️ valores.
# PEP 3102 – Keyword-Only Arguments
# https://peps.python.org/pep-3102/

"""
    Com o "*" tem que ser nomeados os argumentos
    apos o "*" como esta mostando abaixo.

"""


def somar(x, y, *, d, e):
    print(x + y + d + e)


# como pode ver o "d" e o "e" estaa sendo nomeado
# porque estão depois do "*" e se não for nomeado
# pode ter um erro.
somar(3, 3, d=3, e=4)

"""
    caso vocẽ use o "*" e nao queira que os argumentos que estão antes do "*"
    que tambem sejão aurgumentos nomeados, podemos evitar dessa forma abaixo
    colocando a barra antes do "*".
"""


def somar(x, y, /, *, d, e):
    print(x + y + d + e)


somar(3, 3, d=3, e=3)
