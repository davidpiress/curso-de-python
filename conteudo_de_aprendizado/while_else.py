# usando while  com else

nome1 = 'davi queiroz pires'
variavel_vazia = ''
i = 0 
while i < len(nome1):
    letra = nome1[i]
    variavel_vazia += letra
    if variavel_vazia == '':
        break
    i += 1
else:
    print(variavel_vazia)


nome = 'daviueirozpires'

i = 0 
while i < len(nome):
    letra = nome[i]
   
    if letra == ' ':
        break
    print(letra)
    i += 1
else:
    print('laço finalizado no espaço')