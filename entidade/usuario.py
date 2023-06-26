from entidade.pessoa import Pessoa


class Usuario(Pessoa):
    def __init__(self, nome: str, cpf: str, telefone: str, sexo: str, nome_usuario: str, senha_usuario: str,  tempo_consulta: int, preco_consulta: float, cargo: str = "Funcionario"):
        super().__init__(nome, cpf, telefone, sexo)
        self.__relatorio = []
        self.__nome_usuario = nome_usuario
        self.__senha_usuario = senha_usuario
        self.__preco_consulta = preco_consulta
        self.__tempo_consulta = tempo_consulta
        self.__cargo = cargo

    @property
    def nome_usuario(self):
        return self.__nome_usuario

    @nome_usuario.setter
    def nome_usuario(self, nome_usuario: str):
        if isinstance(nome_usuario, str):
            self.__nome_usuario = nome_usuario

    @property
    def senha_usuario(self):
        return self.__senha_usuario

    @senha_usuario.setter
    def senha_usuario(self, senha_usuario: str):
        if isinstance(senha_usuario, str):
            self.__senha_usuario = senha_usuario

    @property
    def preco_consulta(self):
        return self.__preco_consulta

    @preco_consulta.setter
    def preco_consulta(self, preco_consulta: float):
        if isinstance(preco_consulta, float):
            self.__preco_consulta = preco_consulta

    @property
    def tempo_consulta(self):
        return self.__tempo_consulta

    @tempo_consulta.setter
    def tempo_consulta(self, tempo_consulta:int):
        if isinstance(tempo_consulta, int):
            self.__tempo_consulta = tempo_consulta

    @property
    def relatorio(self):
        return self.__relatorio

    def atualiza_atributo(self, atributo, valor):
        setattr(self, atributo, valor)
