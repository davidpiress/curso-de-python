"""
    Higher Order Functions
    funções de primeira Classe

"""


def saudacao(nome, sobrenome, msg):
    return nome, sobrenome, msg

def executa(funcao, nome, sobrenome,msg):
    return funcao(nome, sobrenome, msg)

v = executa(saudacao, 'davi', 'queiroz','boom dia')
print(*v)

print()

def saudacao(nome, sobrenome, msg):
    return nome, sobrenome, msg

def executa(funcao, *args):
    return funcao(*args)

v = executa(saudacao, 'davi', 'queiroz','boom dia')
print(*v)

print()

def saudacao(msg):
    return msg

def executa(funcao, msg):
    return funcao(msg)

v = executa(saudacao, 'davi queiroz boom dia')
print(v)