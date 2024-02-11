# groupby - agrupando valores (itertools)
from itertools import groupby

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]

lista = ['a', 'a', 'a', 'a', 'b', 'c', 'a']
grupos = groupby(sorted(lista))

for chave, grupo in grupos:
    print(chave)
    print(list(grupo))

print()

def ordenar(aluno):
    return aluno['nota']


grupo_alunos = sorted(alunos, key=ordenar)
alunos_agrupados = groupby(grupo_alunos, key=ordenar)


for chave, grupo in alunos_agrupados:
    print(chave)
    for aluno in grupo:
        print(aluno)

