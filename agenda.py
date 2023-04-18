

class Agenda:
    def __int__(self, hora_de_entrada: int, hora_intervalo_entrada: int,
                hora_intervalo_saida: int, hora_de_saida: int):
        if isinstance(hora_de_entrada, int) and isinstance(hora_intervalo_entrada, int)\
                and isinstance(hora_intervalo_saida, int) and isinstance(hora_de_saida, int):
            self.__hora_de_entrada = hora_de_entrada
            self.__hora_intervalo_entrada = hora_intervalo_entrada
            self.__hora_intervalo_saida = hora_intervalo_saida
            self.__hora_de_saida = hora_de_saida
            self.__agenda = []

    @property
    def hora_de_entrada(self):
        return self.__hora_de_entrada

    @hora_de_entrada.setter
    def hora_de_entrada(self, hora_de_entrada: int):
        if isinstance(hora_de_entrada, int):
            self.__hora_de_entrada = hora_de_entrada

    @property
    def hora_intervalo_entrada(self):
        return self.__hora_intervalo_entrada

    @hora_intervalo_entrada.setter
    def hora_intervalo_entrada(self, hora_intervalo_entrada: int):
        if isinstance(hora_intervalo_entrada, int):
            self.__hora_intervalo_entrada = hora_intervalo_entrada

    @property
    def hora_intervalo_saida(self):
        return self.__hora_intervalo_saida

    @hora_intervalo_saida.setter
    def hora_intervalo_saida(self, hora_intervalo_saida: int):
        if isinstance(hora_intervalo_saida, int):
            self.__hora_intervalo_saida = hora_intervalo_saida

    @property
    def hora_de_saida(self):
        return self.__hora_de_saida

    def hora_de_saida(self, hora_de_saida: int):
        if isinstance(hora_de_saida, int):
            self.__hora_de_saida = hora_de_saida

    @property
    def agenda(self):
        return self.__agenda

    def agenda(self, consulta: Consulta):
        if isinstance(consulta, Consulta):
            for i in self.__agenda:
                if(i == consulta):
                    self.__agenda.remove(consulta)
                    return f"{consulta} consulta removida da agenda"
            self.__agenda.append(consulta)
            return f"{consulta} consulta adicionada a agenda"
