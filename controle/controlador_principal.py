from limite.tela_principal import TelaPrincipal
from controle.controlador_cliente import ControladorClientes
from controle.controlador_consulta import ControladorConsulta
from controle.controlador_agenda import ControladorAgenda
from controle.controlador_usuario import ControladorUsuario
from controle.controlador_login import ControladorLogin


class ControladorPrincipal:
    def __init__(self):
        self.__controlador_usuario = ControladorUsuario(self)
        self.__controlador_agenda = ControladorAgenda(self)
        self.__controlador_login = ControladorLogin(self)
        self.__controlador_cliente = ControladorClientes(self)
        self.__controlador_consulta = ControladorConsulta(self)
        self.__tela_principal = TelaPrincipal(self)

    @property
    def controlador_usuario(self):
        return self.__controlador_usuario

    @property
    def controlador_cliente(self):
        return self.__controlador_cliente

    @property
    def controlador_agenda(self):
        return self.__controlador_agenda

    @property
    def controlador_consulta(self):
        return self.__controlador_consulta

    @property
    def controlador_login(self):
        return self.__controlador_login

    def inicia_sistema(self):
        self.controlador_login.abrir_tela()

    def abrir_tela(self):
        self.__tela_principal.open()
