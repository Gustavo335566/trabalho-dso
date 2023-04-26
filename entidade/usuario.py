from entidade.pessoa import Pessoa
from entidade.agenda import Agenda


class Usuario(Pessoa, Agenda):
    def __int__(self, nome_usuario: str, senha: str, id_usuario: int,
                hora_de_entrada: int, hora_intervalo_entrada: int,
                hora_intervalo_saida: int, hora_de_saida: int):
        if isinstance(nome_usuario, str) and isinstance(senha, int)\
                and isinstance(id_usuario, int):
            self.__nome_usuario = nome_usuario
            self.__senha = senha
            self.__hitorico_medico = []
            self.__id_usuario = id_usuario
            self.__agenda = Agenda(hora_de_entrada, hora_intervalo_entrada, hora_intervalo_saida, hora_de_saida)

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

    def historico_medico(self, consulta: Consulta):
        if isinstance(consulta, Consulta):
            for i in self.__hitorico_medico:
                if(i == consulta):
                    self.__hitorico_medico.remove(consulta)
                    return f"{consulta} removida"
            self.__hitorico_medico.append(consulta)
            return f"{consulta} adicionada"
