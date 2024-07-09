# Métodos úteis dos dicionários em Python
pessoa = {
    'nome': 'davi',
    'sobrenome': 'pires',
}

# len - quantas chaves
print(len(pessoa))
# keys - iterável com as chaves
for chave in pessoa.keys():
    print(chave)
# values - iterável com os valores
for valor in pessoa.values():
    print(valor)
# items - iterável com chaves e valores
for nome, sobrenome in pessoa.items():
    print(nome, sobrenome)
# setdefault - adiciona valor se a chave não existe
pessoa.setdefault('altura', 1.90)
print(pessoa['altura'])
# copy - retorna uma cópia rasa (shallow copy)
print()
import copy
d1 = {
    'd': 1,
    'e': 2,
    'f': [3, 2, 2, 1],
}

d2 = copy.deepcopy(d1)
print(d2)
d3 = d1.copy()
d3 = d2.update(letra='y')
print(d1)
print(d2)

print()
# get - obtém uma chave

print(pessoa.get('nome'))
    
# pop - Apaga um item com a chave especificada (del)
nome = pessoa.pop('nome')
print(nome)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
pessoa.update(idade=29)
for v, i in pessoa.items():
    print(v, i)
