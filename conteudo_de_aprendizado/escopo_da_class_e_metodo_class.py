# Escopo da class e metodo da class
class Animal:
    def __init__(self, nome):
        self.nome = nome

        variavel = 'valor'
        print(variavel)

    def comendo(self, comendo):
        return f'{self.nome} esta comendo {comendo}.'

    def executar(self, *args, **kwargs):
        return self.comendo(*args, **kwargs)


leao = Animal('Leão')
print(leao.nome)
print(leao.executar('carne'))
