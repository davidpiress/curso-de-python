"""
    Tratamento de erro com try e except e para não deixa que os erros
    aconteça silenciosamente para saber do que se trata
"""
# ex:
"""a = 5
b = 0
print(a / b)"""

# Ao executar o print percebemos um erro que se chama ZeroDivisionError: division by zero
# tratamento de erros mas não e uma boa pratica de programação

try:
    a = 5
    b = 0
    print(a / b)
except:
    print('erro tratado\nZeroDivisionError: division by zero')

# Forma correta e decobrir qual e o erro e e usar junto execept,
# Exemplo
print()
try:
    a = 5
    b = 0
    print(a / b)
except ZeroDivisionError:
    print('O numero não pode ser dividido por zero')


print()
# podemos uasr o finally mas sempre sera executado.
# exemplo:
try:
    print(10 / 1)
except ZeroDivisionError:
    print('nao pode ser divido por 0')
else:
    print('else execuatado')
finally:
    print('sempre sera execuatdo')


# O sistema de exceções do Python funciona da seguinte maneira: quando uma
# exceção é lançada (raise), o interpretador entra em estado de alerta e vai
# ver se o método atual toma alguma precaução ao tentar executar esse trecho de código
# quando você mesmo  cria as exceções.
# exemplo:

def nao_pode_str(y):
    if y == 0:
        raise ZeroDivisionError('Zero não e divisivel por 0.')

def deve_ser_int_float(n, y):
    if not isinstance(n, (float, int)):
        raise TypeError(f'{n} deve ser int ou float')
    if not isinstance(y, (float, int)):
        raise TypeError(f'{y} deve ser int ou float')

def imprimir_nome(n, y):
    deve_ser_int_float(n, y)
    nao_pode_str(y)
    return n / y

print(imprimir_nome(8, '0'))



import generator_expression


print()




















