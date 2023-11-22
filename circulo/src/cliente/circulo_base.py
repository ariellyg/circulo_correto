from abc import ABC, abstractmethod


class CirculoBase(ABC):

    def __init__(self, id: str, limite: int):
        self.id = id
        self.limite = limite

    @abstractmethod
    def setLimite(self, limite: int):
        pass

    def getId(self):
        return self.id

    def getLimite(self):
        return self.limite

    @abstractmethod
    def getNumberOfContacts(self):
        pass