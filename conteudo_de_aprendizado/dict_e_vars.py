#__dict__ e vars para atribuos de instancia

class Pessoa:

    ano = 2024

    def __init__(self, nome, idade):
       self.nome = nome
       self.idade = idade
       

    def ano_nascimento(self):
        return self.ano - self.idade

dados = {'nome': 'davi', 'idade':1}
p1 = Pessoa(**dados)
#atrinuto_p1 = p1.__dict__
#print(p1.__dict__) # colocando p1.__dict__  vai  ver um dicionario 
print(vars(p1))


       
