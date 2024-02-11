"""
    Python tem objetos mutáveis e imutáveis. Os mutáveis contêm estado interno,
    como atributos, que podem ser alterados durante sua existência. Já os imutáveis
    não podem ser alterados e seu estado pode ser definido somente em sua inicialização.
"""


# Problemas dos parametros mutaveis em funções python
# Errado
def adiciona_cliente(nome, lista=[]):  # função criado com parametros nome e lista=[]
    lista.append(nome)  # agora esta adicinando dentro dessa lista vazia com append um valor que sera dado como nome
    return lista  # sera retornado lista com o nome dessa forma ['davi']


adicionando = adiciona_cliente('davi')  # aonde o valor sera enserido e a função jogada para variavel adicionando
# e sem ele você tera um erro caso não tenha valor
adiciona_cliente('juliaa', adicionando)  # usando a função com o valor e variavel a onde foi jogada a função
adiciona_cliente('jessica', adicionando)
adiciona_cliente('vanderson', adicionando)
print(adicionando)  # aqui so sera printado apos valor ser passado pela função toda
print()


# o certo abaixo:
def adicionando2_clinete(nome, lista=None):  # função criado com parametros nome e lista=None
    if lista is None:  # se a lista e None(não valor) entao
        lista = []  # sera regerado outra lista
    lista.append(nome)  # sera adicionado com append
    return lista  # sera retornado lista com o nome dessa forma ['davi']


lista__ = []  # lista vazia para ser adicionado passando pela função e não sera usado a lista de dentro da função
adicionando2 = adicionando2_clinete('mara', lista__)  # aonde o valor sera enserido junto co lista vazio criado por fora
adicionando2_clinete('maria', adicionando2)
adicionando2_clinete('vaania', adicionando2)
adicionando2_clinete('alice', adicionando2)
adicionando2_clinete('marta', adicionando2)
print(adicionando2)  # aqui so sera printado apos valor ser passado pela função toda

print()


def lista_clientes(nome, lista):  # função criada com parametros nome e lista
    lista.append(nome)  # agora esta adicinando dentro dessa lista vazia com append um valor que sera dado como nome
    return lista  # sera retornado lista com o nome dessa forma ['davi']


lista_de_clientes = []

add_lista = lista_clientes('julia', lista_de_clientes)  # aonde o valor sera enserido junto com lista vazio criado
# por fora
lista_clientes('jana', add_lista)  # usando a função com o valor e variavel a onde foi jogada a função
lista_clientes('JUNA', add_lista)
lista_clientes('JAKEN', add_lista)
print(add_lista)  # aqui so sera printado apos valor ser passado pela função toda
