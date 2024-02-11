# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.

"""
def funcao_decoradora(func):        # Esta função e decoradora  e exister clouser que
    def interna(*args, **kwargs):   # que se refere a uma função interna
        for arg in args:
            is_string(arg)
        resultado = func(*args, **kwargs)
        return resultado
    return interna

@funcao_decoradora
def inverter_string(string):
    return string[::-1]

def is_string(param):
    if not isinstance(param, str):
        raise TypeError('Não uma string')

inverter2 = inverter_string('123')
print(inverter2)

string_invertida = funcao_decoradora(inverter_string)
inverter = string_invertida('12')
print(inverter)"""

# DECORADORES COM PARAMETROS

def fabrica_de_decoradora(a=None, b=None, c=None):
    def fabrica_de_funcao(func):
        print('decoradora')
        def aninhada(*args, **kwargs):
            print('aninhada')
            res = func(*args, **kwargs)
            return res
        return aninhada
    return fabrica_de_funcao


@fabrica_de_decoradora(1, 2, 3)
def soma(x, y):
    return x + y


multiplica = fabrica_de_decoradora(1, 2, 3)(lambda x, y: x * y)
print(multiplica(10, 5))
soma_dez_mais_cinco = soma(10, 5)
print(soma_dez_mais_cinco)


print()


def fabrica_de_decoradores(a=None, b=None, c=None):
    def fabrica_de_funcao(func):
        print('decorado')
        def aninhada(*args, **kwargs):
            print('aninhada')
            invertida = func(*args, **kwargs)
            return invertida
        return aninhada
    return fabrica_de_funcao


@fabrica_de_decoradora(1, 2, 3)
def is_stirng(string):
    return string[::-1]

@fabrica_de_decoradora(1, 2, 3)
def soma(x, y):
    return x + y


multiplica = fabrica_de_decoradora(1, 2, 3)(lambda x, y: x * y)
print(multiplica(10, 10))
string_invertida = is_stirng('123456')
print(string_invertida)
resultado = soma(4, 4)
print(resultado)




print()

def funcao_decoradora(nome):
    def criado_de_funcao(func):
        def interna(*args, **kwargs):
            resp = func(*args, **kwargs)
            final = f'{resp}, {nome}'
            return final
        return interna
    return criado_de_funcao

@funcao_decoradora(nome='primeiro')
def soma(x, y):
    return x + y

resultado_da_soma = soma(3000, 3000)
print(resultado_da_soma)




































































