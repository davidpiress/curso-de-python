# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.
# string = 'Luiz'  # str
# print(string.upper())
# print(isinstance(string, str))

class Pessoas:              # temos uma class que o nome chamado Pessoas que e considerado um PascalCase
    ...

p1 = Pessoas()              # crio uma variavel "p1" e jogo para essa varivel o nome da class Pessoas
p1.nome = 'Davi'            # agora dentro da varievel "p1" jogo a variavell nomeque contem o valor 'Davi'
p1.sobrenome = 'Pires'      # da mesma forma dentro da varievel "p1" jogo a variavell sobrenome que contem o valor 'Pires'
print(p1.nome)              # vamos printar o que contem dentro "p1"(class Pessoas) que contem a variavel nome
print(p1.sobrenome)         # vamos printar o que contem dentro "p1"(class Pessoas) que contem a variavel sobrenome
print()

"""
    Como podemos ver abaixo vamos usar o __init__ 
    com self e criar parametros dentro com nome e sobrenome
    e depois passar para o self --> self.nome = nome e self.sobrenome = sobrenome
    os valores dentro p2 = Pessaos2('DAVI', 'PIRES') e com isso printar.
"""
class Pessaos2:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

p2 = Pessaos2('DAVI', 'PIRES')

print(p2.nome)
print(p2.sobrenome)
