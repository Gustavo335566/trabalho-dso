from limite.tela_principal import TelaPrincipal
from controle.controlador_cliente import ControladorClientes
from controle.controlador_consulta import ControladorConsulta
from controle.controladoragenda import ControladorAgenda
from controle.controladorusuario import ControladorUsuario

class ControladorPrincipal:
    def __init__(self):
        self.__controlador_cliente = ControladorClientes(self)
        self.__controlador_consulta = ControladorConsulta(self)
        self.__controlador_agenda = ControladorAgenda(self)
        self.__controlador_usuario = ControladorUsuario(self)
        self.__tela_principal = TelaPrincipal(self)

    def menu_clientes(self):
        self.__controlador_cliente.mostra_menu_clientes()

    def menu_consulta(self):
        self.__controlador_consulta.mostra_menu_consulta()

    def inicia_sistema(self):
        self.abre_tela()

    def encerra_sistema(self):
        exit(0)

    def teste_login(self):
        if(len(self.__controlador_usuario.todos_usuarios) == 0):
            self.__controlador_usuario.cadastro_usuario()
        else:
            self.__controlador_usuario.busca_usuario_nome_senha(TelaPrincipal.tela_login())

    def abre_tela(self):
        lista_opcoes = {1: self.teste_login(), 2: self.__controlador_usuario.cadastro_usuario(), 0: self.encerra_sistema}
        while True:
            opcao = self.__tela_principal.lista_opcoes()
            funcao = lista_opcoes[opcao]
            funcao()
