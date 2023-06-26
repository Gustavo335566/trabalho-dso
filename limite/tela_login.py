import PySimpleGUI as sg


class TelaLogin:
    def __init__(self, controlador_login):
        self.__controlador_login = controlador_login
        self.__window = None

    def open(self):
        self.init_components()
        while True:
            existe = False
            event, value = self.__window.read()
            if event == "Sair" or event == sg.WIN_CLOSED:
                break
            elif event == "Entrar":
                existe = self.__controlador_login.verifica_usuario(value["-IT_USUARIO-"], value["-IT_SENHA-"])
                if existe:
                    self.__window.hide()
                    self.__controlador_login.controlador_principal.abrir_tela()
                    self.__window.un_hide()
                elif not existe:
                    self.mostra_mensagem("ERRO DE LOGIN",
                                         "USUARIO NÃO ENCONTRADO, VERIFIQUE A SENHA OU NOME DE USUARIO")
            elif event == "Registrar":
                self.open_registro_usuario()
        self.close()

    def init_components(self):
        sg.theme("DarkBrown")
        layout = [[sg.Text("Login", size=(40, 3), font="Arial", justification="center")],
                  [sg.Text("Usuario", size=(15, 1)), sg.InputText(size=(15, 1), key="-IT_USUARIO-")],
                  [sg.Text("Senha", size=(15, 1)), sg.InputText(size=(15, 1), key="-IT_SENHA-", password_char="*")],
                  [sg.Button("Entrar"), sg.Button("Registrar"), sg.Push(), sg.Button("Sair")]
                  ]
        self.__window = sg.Window("Tela Principal").Layout(layout)

    def close(self):
        self.__window.close()

    def mostra_mensagem(self, titulo: str, mensagem: str):
        sg.Popup(titulo, mensagem)

    def open_registro_usuario(self):
        self.__controlador_login.controlador_principal.controlador_usuario.tela_usuario.open_tela_cadastro_usuario()
