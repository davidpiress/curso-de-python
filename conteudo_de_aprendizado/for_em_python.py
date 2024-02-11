"""
    'for' e um iterador de valores
    Com o 'for' fica mais pratico para ser iterado 
    dentro de um codigo, apesar e ser importe o while
"""

# Exemplo
"""palavra = 'python'
nova_palavra = ''

for letra in palavra:
    nova_palavra += f'*{letra}'
    print(letra)

print(f'{nova_palavra}*')

"""
palavra = 'davi'
nova_palavra = ''
i = 0 

for letra in palavra:
    nova_palavra += letra
 
    i += 1
print(nova_palavra)

nome = 'marta aparecida'
nome_vazio = ''
y = 0

while y < len(nome):
    letra = nome[y]
    nome_vazio += letra

    y +=1
print(nome_vazio)