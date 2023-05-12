from limite.tela_principal import TelaPrincipal
from controle.controlador_cliente import ControladorClientes
from controle.controlador_consulta import ControladorConsulta


class ControladorPrincipal:
    def __init__(self):
        self.__controlador_cliente = ControladorClientes(self)
        self.__controlador_consulta = ControladorConsulta(self)
        self.__tela_principal = TelaPrincipal(self)

    @property
    def controlador_cliente(self):
        return self.__controlador_cliente

    def menu_clientes(self):
        self.__controlador_cliente.mostra_menu_clientes()

    def menu_consulta(self):
        self.__controlador_consulta.mostra_menu_consulta()

    def inicia_sistema(self):
        self.abre_tela()

    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {1: self.menu_clientes, 2: self.menu_consulta, 0: self.encerra_sistema}
        while True:
            opcao = self.__tela_principal.lista_opcoes()
            funcao = lista_opcoes[opcao]
            funcao()
