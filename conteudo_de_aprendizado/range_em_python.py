# for + range
# range -> range(start(começo), stop(final), 
# step(pelundo de 2 em 2 ou mais))

"""
novo_numero = ''

for i in range(-0,-10,-2):
    i = str(i)
    numeros = i
    novo_numero += numeros
    novo_numero += ' '
print(f'{novo_numero}')


numeros = range(10)

for numero in numeros:
    print(numero)
print()

numeros1 =iter(range(4))

try:
    print(next(numeros1))
    print(next(numeros1))
    print(next(numeros1))
    print(next(numeros1))
    #print(next(numeros1))
except StopIteration:
    print('next ultrapassou a qtd do iterador')"""
    
    
i = 0

for i in range(10):
    if i == 2:
        print('vc pulou o 2')
        continue # volta para o começo do laço que e 
                 # for e depois vai para o outro if abaixo -> if i == 8

    if i == 8:
        print('vc pulou o 8')
        break

    for j in range(1, 3):
        print(i, j)
else:
    print('else executado com sucesso')