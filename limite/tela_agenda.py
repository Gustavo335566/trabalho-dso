import PySimpleGUI as sg


class TelaAgenda:
    def __init__(self, controlador):
        self.__controlador = controlador
        self.__window = None

    def open(self):
        self.init_components()
        while True:
            event, value = self.__window.read()
            if event == "Voltar" or event == sg.WIN_CLOSED:
                break
            elif event == "-BT_CADASTRO_CONSULTA-":
                self.__window.hide()
                self.__controlador.inclui_consulta()
        self.close()



    def init_components(self):
        sg.theme("DarkBrown")
        valores = self.__controlador.mostrar_horarios()
        headings = ["Hora", "Segunda", "Terça", "Quarta", "Quinta", "Sexta"]
        layout = [[sg.Text("AGENDA", size=(40, 1), font=("Arial Bold", 18), justification="center")],
                  [sg.Table(values=valores, headings=headings, justification="center", key="-TABLE-")],
                  [sg.Button("Voltar"), sg.Push(), sg.Button("Cadastrar Consulta", key="-BT_CADASTRO_CONSULTA-")]
                  ]
        self.__window = sg.Window("Tela Principal", size=(420, 280), finalize=True).Layout(layout)

    def open_cadastro_consulta(self):
        self.tela_cadastro_consulta()
        while True:
            event, value = self.__window.read()
            if event == "Cancelar" or event == sg.WIN_CLOSED:
                break
            elif event == "-BT_CONFIRMAR_CADASTRO-":
                self.__window.close()
                return {"cpf": value["-IT_CPF_CLIENTE-"], "hora": value["COMBO_HORA"], "data": value["COMBO_DATA"]}
        self.close()

    def tela_cadastro_consulta(self):
        sg.theme("DarkBrown")
        valores = self.__controlador.mostrar_horarios()
        horarios = [hora[0] for hora in valores]
        layout = [[sg.Text("AGENDA", size=(40, 1), font=("Arial Bold", 18), justification="center")],
                  [sg.Combo(horarios, key="COMBO_HORA"),
                   sg.Combo(["Segunda", "Terça", "Quarta", "Quinta", "Sexta"], key="COMBO_DATA"),
                   sg.Text("CPF"), sg.InputText(size=(11,1), key="-IT_CPF_CLIENTE-"),
                   [sg.Button("Cancelar"), sg.Push(), sg.Button("Confirmar Cadastro", key="-BT_CONFIRMAR_CADASTRO-")]]
                  ]
        self.__window = sg.Window("Cadastro Consulta", size=(420, 280)).Layout(layout)

    def close(self):
        self.__window.close()

    def mostra_mensagem(self, titulo: str, mensagem: str):
        sg.Popup(titulo, mensagem)

    def imprimir(self, hora, consulta):
        print(f"{hora} : {consulta}")

    def imprimir_consulta(self, consulta):
        print(consulta)

    def mostra_mensagem(self, mensagem):
        print(mensagem)
