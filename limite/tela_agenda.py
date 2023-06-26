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
            elif event == "-BT_BUSCAR-":
                self.__window.Hide()
                dados_consulta = self.__controlador.buscar_consulta(value["-IT_CODIGO_CONSULTA-"])
                self.close()
        self.close()

    def init_components(self):
        sg.theme("DarkBrown")
        valores = self.__controlador.mostrar_horarios()
        headings = ["Hora", "Segunda", "Terça", "Quarta", "Quinta", "Sexta"]
        layout = [[sg.Text("AGENDA", size=(40, 1), font=("Arial Bold", 18), justification="center")],
                  [sg.Table(values=valores, headings=headings, justification="center", key="-TABLE-")],
                  [sg.Button("Voltar"), sg.Push(), sg.InputText(size=(4,1), key="-IT_CODIGO_CONSULTA-"),
                   sg.Button("Buscar", key="-BT_BUSCAR-"),
                   sg.Button("Cadastrar Consulta", key="-BT_CADASTRO_CONSULTA-")]
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

    def open_dados_consulta(self, dados_consulta):
        self.tela_dados_consulta(dados_consulta)
        while True:
            event, value = self.__window.read()
            if event == "Voltar" or event == sg.WIN_CLOSED:
                break
            elif event == "-BT_EXCLUIR_CONSULTA-":
                self.__controlador.exclui_consulta(dados_consulta["codigo"])
                self.close()
            elif event == "-BT_FINALIZAR_CONSULTA-":
                self.__controlador.consulta_feita(dados_consulta)
                self.close()
        self.close()

    def tela_dados_consulta(self, dados_consulta):
        layout = [[sg.Text(f'CODIGO:{dados_consulta["codigo"]}', size=(40, 1), font="Arial")],
                  [sg.Text(f'NOME:{dados_consulta["nome"]}', size=(40, 1), font="Arial")],
                  [sg.Text(f'CPF: {dados_consulta["cpf"]}', size=(40, 1), font="Arial")],
                  [sg.Text(f'DATA: {dados_consulta["data"]}', size=(14, 1), font="Arial"),
                  sg.Text(f'HORA: {dados_consulta["hora"]}', size=(10, 1), font="Arial")],
                  [sg.Button("Voltar"), sg.Button("Excluir Consulta", key="-BT_EXCLUIR_CONSULTA-"),
                   sg.Button("Finalizar Consulta", key="-BT_FINALIZAR_CONSULTA-")]
                  ]
        self.__window = sg.Window("Menu Consulta", size=(420, 280)).Layout(layout)

    def close(self):
        self.__window.close()

    def mostra_mensagem(self, titulo: str, mensagem: str):
        sg.Popup(titulo, mensagem)
