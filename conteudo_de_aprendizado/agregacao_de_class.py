# Relações entre classes: associação, agregação e composição
# Associação é um tipo de relação onde os objetos
# estão ligados dentro do sistema.
# Essa é a relação mais comum entre objetos e tem subconjuntos
# como agregação e composição (que veremos depois).
# Geralmente, temos uma associação quando um objeto tem
# um atributo que referencia outro objeto.
# A associação não especifica como um objeto controla
# o ciclo de vida de outro objeto.


class Carrinho:
    def __init__(self):
        self._produtos = []

    def inserir_produtos(self, *produtos):
        # self._produtos.extend(produtos)
        # self._produtos += produtos
        for produto in produtos:
            self._produtos.append(produto)

    def listar_produtos(self):
        for produto in self._produtos:
            print(produto.nome, produto.preco)

    def total(self):
        return sum([p.preco for p in self._produtos])


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

carrinho = Carrinho()
p1, p2 = Produto('Banana', 1.2), Produto('Banana', 1.2)
carrinho.inserir_produtos(p1, p2)
carrinho.listar_produtos()
print(carrinho.total())