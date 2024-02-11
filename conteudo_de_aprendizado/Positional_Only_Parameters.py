# Positional-Only Parameters (/) e Keyword-Only Arguments (*)
# *args (ilimitado de argumentos posicionais)
# **kwargs (ilimitado de argumentos nomeados)
# 🟢 Positional-only Parameters (/) - Tudo antes da barra deve
# ser ❗️APENAS❗️ posicional.
# PEP 570 – Python Positional-Only Parameters
# https://peps.python.org/pep-0570/

"""
    Pode somar no exemplo abaixo com mais de dois argumentos
    apos "/" como você pode ver abaixo e não precisa ser nomeado e
    se tiver que ser so poder ser o ultimo parametro como "e=3".
"""


def somar(x, y, /, d, e):
    print(x + y + d + e)


somar(3, 3, 3, 3)


