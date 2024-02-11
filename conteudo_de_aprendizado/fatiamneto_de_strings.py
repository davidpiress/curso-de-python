"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd
de caracteres da str
"""

#                                0123456789........
buscando_indice_de_uma_string = 'Davi Queiroz Pires'
#                          .....-987654321
print(buscando_indice_de_uma_string[0:8])  # crescente
print(buscando_indice_de_uma_string[-9:-3])  # descrecente
print(buscando_indice_de_uma_string[0:8:2])  # pulando de 2 em 2
print(len(buscando_indice_de_uma_string))    # quantidade de caracteres


print()
nome_string = 'davi pires'
abc_no_meio = f'{nome_string[:2]}ABC{nome_string[5:11]}'
print(abc_no_meio)