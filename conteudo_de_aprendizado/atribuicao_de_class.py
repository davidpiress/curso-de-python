# Atributo de class

#   Com o atributo fora da class podemos usar em mais de uma class
ano_nascimento1 = 2024
class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def ano_nascimento(self):
        #print(f'{self.nome} nasceu no ano de {self.ano_nascimento1 - self.idade}')
        return ano_nascimento1 - self.idade

        

p1 = Pessoa('DAVI', 30)
p2 = Pessoa('marta', 33)
p1.idade += 10
p2.idade += 10
print(p1.ano_nascimento())
print(p2.ano_nascimento())

print()

# Podemos usar tambem o atributo que so vai pertencer a uma class que 
#fica dentro de uma  class
class Pesssa2:

    ano = 2024

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.ano = 2024

    def ano_nascimento2(self):
        print(self.nome)
        return Pesssa2.ano - self.idade


c2 = Pesssa2('marta', 33)
print(c2.ano_nascimento2())
