from objetos_midia.Midia import Midia


class Serie(Midia):
    def __init__(self, nome: str, ano: int, temporadas: int):
        super().__init__(nome, ano)
        self.temporadas = temporadas
        self.spinoff_of = None
        self.__spinoffs = []

    def add_spinoff(self, spinoff: 'Serie'):
        spinoff.spinoff_of = self
        self.__spinoffs.append(spinoff)

    def has_spinoffs(self):
        print('Sim:' if len(self.__spinoffs) else 'Não', *self.__spinoffs)
