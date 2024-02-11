# Operador lógico "not"
# Usado para inverter expressões
print(not False)
print(not True)


"""
    Condição sem o not como vemos abaixo
"""
nome = input('Digite seu nome: ')

if nome == 'davi':
    print('nome correspondente')
else:
    print('nome não correspondente')

"""
    Como podemos ver o com o mesmo codigo feito abaixo
    usando "not" veremos que a condição sera ao contrario
    caso você digite o nome e o else sera executado como a 
    condição verdadeiro.
"""

nome1 = input('Digite seu nome: ')

if not nome1 == 'davi':
    print('nome correspondente')
else:
    print('nome não correspondente')