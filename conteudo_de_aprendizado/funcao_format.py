"""
    Com o format podemos antes das
    variaveis que estão na função format
    acrescentar dentro → 'a={} b={} c={}'
    resultado -> a=a1 b=b2 c=c3
"""

a = 'a1'
b = 'b2'
c = 1.1

formate1 = 'a={} b={} c={}'.format(a, b, c)
print(formate1)

"""
    Outra forma se usar a função format 
    usando os indices
"""
print()
strings = 'a={0} b={1} c={2:.2f}'
formate2 = strings.format(a, b, c)
print(formate2)

"""
    Agora com argumentos nomeados que vai ter o mesmo resultado
"""
print()
strings1 = 'a={nomeado1} b={nomeado2} c={nomeado3}'
formate3 = strings1.format(nomeado1=a, nomeado2=b, nomeado3=c)
print(formate3)
