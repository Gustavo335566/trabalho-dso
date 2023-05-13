from entidade.pessoa import Pessoa


class Cliente(Pessoa):
    def __init__(self, nome: str, cpf: str, telefone: str, sexo: str):
        super().__init__(nome, cpf, telefone, sexo)
        self.__historico = []

    @property
    def historico(self):
        return self.__historico

    def atualiza_atributo(self, atributo, valor):
        setattr(self, atributo, valor)

    def __str__(self):
        return f"Cliente {self.nome} com CPF {self.cpf}"
