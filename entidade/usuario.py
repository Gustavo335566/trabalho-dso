from entidade.pessoa import Pessoa
from entidade.agenda import Agenda


class Usuario(Pessoa, Agenda):
    def __int__(self, nome_usuario: str, senha: str, id_usuario: int):
        if isinstance(nome_usuario, str) and isinstance(senha, int)\
                and isinstance(id_usuario, int):
            self.__nome_usuario = nome_usuario
            self.__senha = senha
            self.__hitorico_medico = []
            self.__id_usuario = id_usuario
            self.__agenda = Agenda()

    @property
    def nome_usuario(self):
        return self.__nome_usuario

    @nome_usuario.setter
    def nome_usuario(self, nome_usuario: str):
        if isinstance(nome_usuario, str):
            self.__nome_usuario = nome_usuario

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, senha: int):
        if isinstance(senha, int):
            self.__senha = senha

    @property
    def historico_medico(self):
        return self.__hitorico_medico

    def add_historico_medico(self, consulta: Consulta):
        if isinstance(consulta, Consulta):
            for i in self.__hitorico_medico:
                if(i == consulta):
                    return "Consulta ja adicionada"
            self.__hitorico_medico.append(consulta)
            return "Consulta adicionada"

    def delete_historico_medico(self, consulta: Consulta):
        if isinstance(consulta, Consulta):
            for i in self.__hitorico_medico:
                if(i == consulta):
                    self.__hitorico_medico.remove(consulta)
                    return "Consulta removida do historico medico"
            self.__hitorico_medico.append(consulta)
            return "Consulta nao esta no historico medico"
