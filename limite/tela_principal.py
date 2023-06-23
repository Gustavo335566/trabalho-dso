import PySimpleGUI as sg


class TelaPrincipal:
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__window = None

    def open(self):
        self.init_components()
        while True:
            event, value = self.__window.read()
            if event == "Sair" or event == sg.WIN_CLOSED:
                break
            elif event == "-BT_CLIENTE-":
                self.__window.hide()
                self.__controlador_principal.controlador_cliente.abrir_tela()
                self.__window.un_hide()
            elif event == "-BT_AGENDA-":
                self.__window.hide()
                self.__controlador_principal.controlador_agenda.abrir_tela()
                self.__window.un_hide()
            elif event == "-BT_USUARIO-":
                self.__window.hide()
                self.__controlador_principal.controlador_usuario.abrir_tela()
                self.__window.un_hide()
            print(event, value)
        self.close()

    def init_components(self):
        sg.theme("DarkBrown")
        nome_usuario = self.__controlador_principal.controlador_usuario.pega_dados_usuario()["nome"]
        layout = [[sg.Text("MENU INICIAL", size=(40, 1), font=("Arial Bold", 18), justification="center")],
                  [sg.Text(f"Bem-vindo, {nome_usuario} ", size=(30, 2), font=("Arial Bold", 15))],
                  [sg.Push(), sg.Button("Agenda", key="-BT_AGENDA-", size=(15, 1)), sg.Push()],
                  [sg.Push(), sg.Button("Clientes", key="-BT_CLIENTE-", size=(15, 1)), sg.Push()],
                  [sg.Push(), sg.Button("Usuario", key="-BT_USUARIO-", size=(15, 1)), sg.Push()],
                  [sg.Push(), sg.Cancel("Sair", size=(15, 1)), sg.Push()]
                  ]
        self.__window = sg.Window("Tela Principal", size=(420, 280)).Layout(layout)

    def close(self):
        self.__window.close()

    def mostra_mensagem(self, titulo: str, mensagem: str):
        sg.Popup(titulo, mensagem)
