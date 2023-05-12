from entidade.pessoa import Pessoa
from entidade.agenda import Agenda


class Usuario(Pessoa):
    def __int__(self, nome: str, nome_usuario: str, cpf: str, senha_usuario: str, sexo: str, telefone: str,
                tempo_consulta: int, preco_consulta: float):
        if isinstance(nome_usuario, str) and isinstance(senha_usuario, str) and isinstance(nome, str) \
                and isinstance(cpf, str) and isinstance(sexo, str) and isinstance(telefone, str) and isinstance(tempo_consulta, int)\
                and isinstance(preco_consulta, float):
            self.__nome_usuario = nome_usuario
            self.__senha_usuario = senha_usuario
            self.__hitorico = []
            self.__agenda = Agenda(tempo_consulta)
            self.__preco_consulta = preco_consulta
            super.__init__(nome, cpf, telefone, sexo)

    @property
    def nome_usuario(self):
        return self.__nome_usuario

    @nome_usuario.setter
    def nome_usuario(self, nome_usuario: str):
        if isinstance(nome_usuario, str):
            if nome_usuario.isalpha() is False or len(nome_usuario) < 8 or len(nome_usuario) > 20:
                return "Somente letras e tamanho de nome do usuario de 8 a 20 caracteres"
            self.__nome_usuario = nome_usuario
            return "alteracao possivel"

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, senha: str):
        if isinstance(senha, str):
            self.__senha = senha

    @property
    def historico(self):
        return self.__hitorico

    def add_historico(self, consulta: Consulta):
        if isinstance(consulta, Consulta):
            for i in self.__hitorico:
                if(i.horario == consulta.horario and i.cpf == consulta.cpf):
                    return "Consulta ja adicionada"
            self.__hitorico.append(consulta)
            return "Consulta adicionada"

    @property
    def preco_consulta(self):
        return self.__preco_consulta

    @preco_consulta.setter
    def preco_consulta(self, preco_consulta: float):
        if isinstance(preco_consulta, float):
            self.__preco_consulta = preco_consulta
