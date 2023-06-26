from entidade.pessoa import Pessoa


class Cliente(Pessoa):
    def __init__(self, nome: str, cpf: str, telefone: str, sexo: str):
        super().__init__(nome, cpf, telefone, sexo)
        self.__historico = []

    @property
    def historico(self):
        return self.__historico

    def adiciona_no_historico(self, mensagem: str):
        self.__historico.append(mensagem)

    def __str__(self):
        return f"Cliente {self.nome} com CPF {self.cpf}"
