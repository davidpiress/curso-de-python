"""
    closer e funções que retornam outras funções
"""

def saudacao(saudacao):
    def sauda(nome):
        return saudacao, nome
    return sauda # <-- sauda esta sem os parenteses() mais poderia esta.


fala_bom_dia = saudacao('bom dia')
#print(fala_bom_dia()) # <-- com sauda esta sem os parenteses devo colocar no --> 'v'

for nome in ['davi', 'maria', 'joana', 'fernanda']:
    print(*fala_bom_dia(nome))