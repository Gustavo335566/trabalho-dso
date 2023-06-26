import PySimpleGUI as sg
from validate_docbr import CPF


class TelaCliente:
    def __init__(self, controlador):
        self.__controlador = controlador
        self.__window = None

    def pega_observacao(self):
        self.__window = sg.Window("Menu Clientes",
                                  size=(420, 280)).Layout([[sg.InputText(size=(40 ,3), key="Observacao")],
                                                           [sg.Button("Voltar"), sg.Push(), sg.Button("Enviar")]
                                                           ])
        while True:
            event, value = self.__window.read()
            if event == "Voltar" or event == sg.WIN_CLOSED:
                break
            elif event == "Enviar":
                self.close()
                return value["Observacao"]
        self.close()



    def dados_cliente(self, dados_cliente):
        cpf = CPF()
        layout = [[sg.Text(f'NOME:{dados_cliente["nome"]}', size=(40, 1), font="Arial")],
                  [sg.Text(f'CPF: {cpf.mask(dados_cliente["cpf"])}', size=(40, 1), font="Arial")],
                  [sg.Text(f'TELEFONE: {dados_cliente["telefone"]}', size=(40, 1), font="Arial")],
                  [sg.Text(f'SEXO: {dados_cliente["sexo"]}', size=(40, 1), font="Arial")],
                  [sg.Button("Voltar"), sg.Button("Excluir Cliente", key="-BT_EXCLUIR_CLIENTE-"),
                   sg.Button("Alterar Cliente", key="-BT_ALTERAR_CLIENTE-")]
                  ]
        self.__window = sg.Window("Menu Clientes", size=(420, 280)).Layout(layout)

    def open_dados_cliente(self, dados_cliente):
        self.dados_cliente(dados_cliente)
        while True:
            event, value = self.__window.read()
            if event == "Voltar" or event == sg.WIN_CLOSED:
                break
            elif event == "-BT_EXCLUIR_CLIENTE-":
                self.__controlador.exclui_cliente(dados_cliente["cpf"])
                self.close()
            elif event == "-BT_ALTERAR_CLIENTE-":
                self.open_altera_dados_cliente(dados_cliente)
        self.close()


    def open(self):
        self.init_components()
        while True:
            event, value = self.__window.read()
            if event == "Voltar" or event == sg.WIN_CLOSED:
                break
            elif event == "-BT_CADASTRAR_CLIENTE-":
                self.__window.close()
                self.open_tela_cadastro()
            elif event == "-BT_BUSCAR-":
                self.__window.close()
                self.__controlador.busca_cliente(value["-IT_BUSCA-"])
            else:
                self.__window.close()
                self.__controlador.busca_cliente(event)
            print(event, value)
        self.close()

    def init_components(self):
        sg.theme("DarkBrown")
        lista_botao = self.__controlador.listar_clientes()
        layout = [[sg.Text("MENU CLIENTES", size=(40, 2), font=("Arial", 18), justification="center")],
                  [sg.Button("Cadastrar Cliente", key="-BT_CADASTRAR_CLIENTE-"), sg.Push(),
                   sg.InputText(key="-IT_BUSCA-", size=(11, 1), tooltip="Digite o CPF"),
                   sg.Submit("Buscar", key="-BT_BUSCAR-")],
                  [lista_botao],
                  [sg.Button("Voltar", )]
                  ]
        self.__window = sg.Window("Menu Clientes", size=(420, 280)).Layout(layout)

    def tela_cadastro(self):
        sg.theme("DarkBrown")
        layout = [[sg.Text("Digite seu nome", size=(40, 2), font="Arial")],
                  [sg.Text("Nome", size=(15, 1)), sg.InputText(key="-IT_NOME-")],
                  [sg.Text("CPF", size=(15, 1)), sg.InputText(key="-IT_CPF-")],
                  [sg.Text("TELEFONE", size=(15,1)), sg.InputText(key="-IT_TELEFONE-")],
                  [sg.Frame(layout=[
                      [sg.Radio("M", "RADIO1", size=(10, 1), key="it_masc"),
                       sg.Radio("F", "RADIO1", size=(10, 1), key="it_fem")]],
                      title="Sexo", relief=sg.RELIEF_SUNKEN, )],
                  [sg.Submit("Finalizar cadastro"), sg.Button("Voltar")]
                  ]
        self.__window = sg.Window("Cadastro Cliente").Layout(layout)

    def open_tela_cadastro(self):
        self.tela_cadastro()
        while True:
            event, value = self.__window.read()
            if event == "Voltar" or event == sg.WIN_CLOSED:
                break
            elif event == "Finalizar cadastro":
                if not (value["-IT_NOME-"].replace(" ", "")).isalpha():
                    self.mostra_mensagem("Valor Invalido", "ATENÇÃO: FORMATO DE NOME INVALIDO")
                else:
                    cpf = CPF()
                    if not cpf.validate(cpf.mask(value["-IT_CPF-"])):
                        self.mostra_mensagem("Valor Invalido", "ATENÇÃO: CPF NÃO EXISTE")
                    else:
                        if len(value["-IT_TELEFONE-"]) != 11:
                            self.mostra_mensagem("Valor Invalido", "ATENÇÃO: FORMATO DE TELEFONE INVALIDO")
                        else:
                            if value["it_masc"]:
                                sexo = "M"
                            else:
                                sexo = "F"
                            self.__controlador.incluir_cliente({"nome": value["-IT_NOME-"], "cpf": value["-IT_CPF-"],
                                                               "telefone": value["-IT_TELEFONE-"], "sexo": sexo})
                            break
        self.close()

    def tela_altera_dados_cliente(self, dados_cliente):
        sg.theme("DarkBrown")
        if dados_cliente["sexo"] == "M":
            frame_layout = [
                [sg.Radio("M", "RADIO1", size=(10, 1), key="it_masc", default=True),
                 sg.Radio("F", "RADIO1", size=(10, 1), key="it_fem")]]
        else:
            frame_layout = [
                [sg.Radio("M", "RADIO1", size=(10, 1), key="it_masc"),
                 sg.Radio("F", "RADIO1", size=(10, 1), key="it_fem", default=True)]]
        layout = [[sg.Text("Digite seu nome", size=(40, 2), font="Arial")],
                  [sg.Text("Nome", size=(15, 1)), sg.InputText(f'{dados_cliente["nome"]}', key="-IT_NOME-")],
                  [sg.Text("CPF", size=(15, 1)), sg.Text(f'{dados_cliente["cpf"]}', key="-IT_CPF-")],
                  [sg.Text("TELEFONE", size=(15,1)), sg.InputText(f'{dados_cliente["telefone"]}', key="-IT_TELEFONE-")],
                  [sg.Frame(layout=frame_layout, title="Sexo", relief=sg.RELIEF_SUNKEN, )],
                  [sg.Submit("Alterar Dados"), sg.Button("Voltar")]
                  ]
        self.__window = sg.Window("Cadastro Cliente").Layout(layout)

    def open_altera_dados_cliente(self, dados_cliente):
        self.tela_altera_dados_cliente(dados_cliente)
        while True:
            event, value = self.__window.read()
            if event == "Voltar" or event == sg.WIN_CLOSED:
                break
            elif event == "Alterar Dados":
                if not (value["-IT_NOME-"].replace(" ", "")).isalpha():
                    self.mostra_mensagem("Valor Invalido", "ATENÇÃO: FORMATO DE NOME INVALIDO")
                else:
                    if len(value["-IT_TELEFONE-"]) != 11:
                        self.mostra_mensagem("Valor Invalido", "ATENÇÃO: FORMATO DE TELEFONE INVALIDO")
                    else:
                        if value["it_masc"]:
                            sexo = "M"
                        else:
                            sexo = "F"
                        self.__controlador.alterar_cliente(
                            {"nome": value["-IT_NOME-"], "cpf": dados_cliente["cpf"],
                             "telefone": value["-IT_TELEFONE-"], "sexo": sexo})
                        break
        self.close()
    def close(self):
        self.__window.close()

    def mostra_mensagem(self, titulo: str, mensagem: str):
        sg.Popup(titulo, mensagem)
