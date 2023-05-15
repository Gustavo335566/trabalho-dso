from limite.tela_principal import TelaPrincipal
from controle.controlador_cliente import ControladorClientes
from controle.controlador_consulta import ControladorConsulta
from controle.controlador_agenda import ControladorAgenda
from controle.controlador_usuario import ControladorUsuario

class ControladorPrincipal:
    def __init__(self):
        self.__controlador_cliente = ControladorClientes(self)
        self.__controlador_consulta = ControladorConsulta(self)
        self.__controlador_agenda = ControladorAgenda(self)
        self.__controlador_usuario = ControladorUsuario(self)
        self.__tela_principal = TelaPrincipal(self)

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
    def controlador_usuario(self):
        return self.__controlador_usuario

    def inicia_sistema(self):
        self.abre_tela()

    def encerra_sistema(self):
        exit(0)

    def teste_login(self):
        if len(self.__controlador_usuario.todos_usuarios) == 0:
            self.__tela_principal.mostra_mensagem("Nenhum usuario cadastrado! Abrindo cadastramento")
            self.__controlador_usuario.cadastro_usuario()
        else:
            nome_usuario, senha_usuario = self.__tela_principal.tela_login()
            self.__controlador_usuario.busca_usuario_nome_senha(nome_usuario, senha_usuario)

    def abre_tela(self):
        lista_opcoes = {1: self.teste_login, 2: self.__controlador_usuario.cadastro_usuario, 0: self.encerra_sistema}
        while True:
            opcao = self.__tela_principal.lista_opcoes()
            funcao = lista_opcoes[opcao]
            funcao()
