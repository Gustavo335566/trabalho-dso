from limite.tela_login import TelaLogin


class ControladorLogin:
    def __init__(self, controlador_principal):
        self.__tela_login = TelaLogin(self)
        self.__controlador_principal = controlador_principal

    def abrir_tela(self):
        self.__tela_login.open()

    def verifica_usuario(self, nome, senha):
        for usuario in self.__controlador_principal.controlador_usuario.usuario_dao.get_all():
            if usuario.nome_usuario == nome and usuario.senha_usuario == senha:
                self.__controlador_principal.controlador_usuario.usuario_logado = usuario
                agenda = self.__controlador_principal.controlador_agenda.agenda_dao.get(usuario.cpf)
                self.__controlador_principal.controlador_agenda.agenda_usuario_logado = agenda
                return True

    @property
    def controlador_principal(self):
        return self.__controlador_principal
