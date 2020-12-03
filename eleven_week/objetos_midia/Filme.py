from objetos_midia.Midia import Midia
from datetime import datetime


class Filme(Midia):
    def __init__(self, nome: str, ano: int, duracao: float):
        super().__init__(nome, ano)
        self.duracao = duracao
        self.__pre_estreia = None

    def create_pre_estreia(self, data: datetime):
        self.__pre_estreia = data

    def have_pre_estreia(self):
        return self.__pre_estreia
