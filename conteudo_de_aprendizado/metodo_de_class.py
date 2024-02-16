# Métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primeiro
# parâmetro, receberemos a própria classe.

class Pesssoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def nome_e_idade(cls, nome, idade):
        return f'{nome}, {idade}'



p1 = Pesssoa.nome_e_idade('davi', 20)
print(p1)



