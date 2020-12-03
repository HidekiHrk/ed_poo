class Midia:
    def __init__(self, nome: str, ano: int):
        self.nome = nome
        self.ano = ano
        self.likes: int = 0

    def __repr__(self):
        return f'<{self.__class__.__name__}: {self.nome} - {self.ano}>'