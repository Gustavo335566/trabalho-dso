from pessoa import Pessoa


class Medico(Pessoa):
    def __init__(self, nome: str, cpf: int, telefone: int, sexo: str, crm: int):
        super().__init__(nome, cpf, telefone, sexo)
        self.__crm = crm

    @property
    def crm(self):
        return self.__crm

    @crm.setter
    def crm(self, crm):
        if isinstance(crm, Medico) and crm is not None:
            self.__crm = crm

    def __str__(self):
        return f"Dr. {self.__nome} ({self.crm})"
