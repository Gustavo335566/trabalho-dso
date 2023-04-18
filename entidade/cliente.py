from entidade.pessoa import Pessoa


class Cliente(Pessoa):
    def __init__(self, nome: str, cpf: int, telefone: int, sexo: str, id_cliente: int):
        super().__init__(nome, cpf, telefone, sexo)
        self.__id_cliente = id_cliente
        self.__historico = []

    @property
    def id_cliente(self):
        return self.__id_cliente

    @id_cliente.setter
    def id_cliente(self, id_cliente):
        if isinstance(id_cliente, Cliente) and id_cliente is not None:
            self.__id_cliente = id_cliente

    @property
    def historico(self):
        return self.__historico

    @historico.setter
    def historico(self, historico):
        self.__historico = historico

    def __str__(self):
        return f"{self.__id_cliente} | {self.__nome}"
