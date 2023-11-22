from src.cliente.circulo_base import CirculoBase


class Circulo(CirculoBase):

    def __init__(self, id: str, limite: int):
        super().__init__(id, limite)
        self.cttcirculo = []

    def getNumberOfContacts(self):
        return len(self.cttcirculo)

    def getId(self):
        return self.id

    def getLimite(self):
        return self.limite

    def setLimite(self, limite: int):
        self.limite = limite

    def __eq__(self, other):
        return self.id == other.id