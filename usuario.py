from pessoa import Pessoa
from agenda import Agenda


class Usuario(Pessoa, Agenda):
    def __int__(self, usuario: str, senha: str, id_usuario: int,
                hora_de_entrada: int, hora_intervalo_entrada: int,
                hora_intervalo_saida: int, hora_de_saida: int):
        if isinstance(usuario, str) and isinstance(senha, int)\
                and isinstance(id_usuario, int):
            self.__usuario = usuario
            self.__senha = senha
            self.__hitorico_medico = []
            self.__id_usuario = id_usuario
            self.__agenda = Agenda(hora_de_entrada, hora_intervalo_entrada, hora_intervalo_saida, hora_de_saida)

    @property
    def usuario(self):
        return self.__usuario

    @usuario.setter
    def usuario(self, usuario: str):
        if isinstance(usuario, str):
            self.__usuario = usuario

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
