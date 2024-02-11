# Métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primeiro
# parâmetro, receberemos a própria classe.

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def com_string(cls):
        print('usando strinfo com cls')

    @classmethod 
    def metodo_hey(cls, nome):
        return nome, 30


    


p1 = Pessoa()
Pessoa.metodo_hey('maria')
Pessoa.com_string()