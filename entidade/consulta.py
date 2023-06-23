from entidade.cliente import Cliente


class Consulta:
    __PROXIMO_CODIGO = 1000

    def __init__(self, cliente: Cliente, data: int, horario: int):
        if isinstance(cliente, Cliente):
            self.__cliente = cliente
        self.__PROXIMO_CODIGO += 1
        self.__codigo = self.__PROXIMO_CODIGO
        self.__data = data
        self.__horario = horario

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente: Cliente):
        self.__cliente = cliente

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: int):
        self.__codigo = codigo

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data: int = None):
        self.__data = data

    @property
    def horario(self):
        return self.__horario

    @horario.setter
    def horario(self, horario: int):
        self.__horario = horario

    def __str__(self):
        return f"{self.codigo}: Consulta de {self.cliente}. {self.data} {self.horario}"
