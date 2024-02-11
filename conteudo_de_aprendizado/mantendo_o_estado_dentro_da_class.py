# Mantendo estados dentro da classe
class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando


    def nao_filmar(self):
            print(f'{self.nome} nao esta filmando')
            self.filmando = True


    def filmar(self):
        if not self.filmando:
            self.filmando = True
            print(f'{self.nome} esta filmando')

        print(f'{self.nome} JA esta filmando')

    def nao_pode_fotograr(self):
        if self.filmando:
            self.filmando = True
            print(f'{self.nome} não pode fotografar filmando....')

        print(self.nome, 'esta parando de filmar...')

    def fotografando(self):
        print(self.nome, 'estaa fotografando...')






c1 = Camera('sony')
c2 = Camera('canon')
c1.nao_filmar()
c1.filmar()
c1.nao_pode_fotograr()
c1.fotografando()
print()

c2.nao_filmar()
c2.filmar()
c2.nao_pode_fotograr()
c2.fotografando()