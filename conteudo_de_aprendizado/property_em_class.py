# @property - um getter no modo Pythônico
# getter - um método para obter um atributo
# cor -> get_cor()
# modo pythônico - modo do Python de fazer coisas
# @property é uma propriedade do objeto, ela
# é um método que se comporta como um
# atributo 🤯 🤯 🤯
# Geralmente é usada nas seguintes situações:
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Código cliente - é o código que usa seu código


"""
class Caneta:
    def __init__(self, cor1, cor2):
        self.cor_de_tinta = cor1 
        self.cor_de_tinta2 = cor2

    @property
    def cor(self):
        print(self.cor_de_tinta, self.cor_de_tinta2)
        return f'nova cor'

caneta = Caneta('azul', 'verde')
print(caneta.cor)
"""





class Caneta:
    def __init__(self, valor):
        self._caneta_azul = valor

    @property
    def cor(self):
        return self._caneta_azul

    @cor.setter
    def cor(self, valor):
        self._caneta_azul = valor

caneta = Caneta('azul')
caneta.cor = 'vermelho'
print(caneta.cor)





