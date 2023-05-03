from entidade.usuario import Usuario
from entidade.agenda import Agenda
from limite.tela_usuario import Tela_usuario
class Controlador_usuario(Usuario, Agenda, Tela_usuario):
    def __init__(self, controlador_principal: ControladorPrincipal):
        self.__usuarios = []
        self.__tela_usuario = Tela_usuario()
        self.__controlador_principal = controlador_principal
        self.__controlador_cliente = ControladorCliente
