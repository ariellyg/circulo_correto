from src.cliente.contato_base import ContatoBase


class Contato(ContatoBase):

    def __init__(self, id: str, email: str):
        super().__init__(id, email)

    def getId(self):
        return self.id

    def setId(self, id:str):
        self.id = id

    def getEmail(self):
        return self.email

    def setEmail(self, email:str):
        self.email = email

    def __eq__(self, other):
        return self.id == other.id and self.email == other.email