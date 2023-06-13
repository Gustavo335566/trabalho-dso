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
                pass
            elif event == "-BT_USUARIO-":
                pass
            print(event, value)
        self.close()

    def init_components(self):
        sg.theme("DarkBrown")
        layout = [[sg.Text("MENU INICIAL", size=(40, 2), pad=((135, 0), 3), font=("Arial Bold", 18))],
                  [sg.Button("Agenda", key="-BT_AGENDA-", size=(15, 1), pad=((140, 0), 3))],
                  [sg.Button("Clientes", key="-BT_CLIENTE-", size=(15, 1), pad=((140, 0), 3))],
                  [sg.Button("Usuario", key="-BT_USUARIO-", size=(15, 1), pad=((140, 0), 3))],
                  [sg.Cancel("Sair", size=(15, 1), pad=((140, 0), 3))]
                  ]
        self.__window = sg.Window("Tela Principal", size=(420, 280)).Layout(layout)

    def close(self):
        self.__window.close()

    def mostra_mensagem(self, titulo: str, mensagem: str):
        sg.Popup(titulo, mensagem)
