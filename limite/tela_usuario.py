import PySimpleGUI as sg
from validate_docbr import CPF


class TelaUsuario:
    def __init__(self, controlador):
        self.__controlador = controlador
        self.__window = None

    def init_components(self):
        sg.theme("DarkBrown")
        layout = [[sg.Text("MENU USUARIO", size=(40, 2), font="Arial")],
                  [sg.Push(), sg.Button("DADOS DO USUARIO", key="-BT_DADOS_USUARIO-"), sg.Push()],
                  [sg.Push(), sg.Button("RELATORIO FINANCEIRO", key="-BT_FINANCEIRO-"), sg.Push()],
                  [sg.Button("Voltar")]
                  ]
        self.__window = sg.Window("Menu Clientes", size=(420, 280)).Layout(layout)

    def open(self):
        self.init_components()
        while True:
            event, value = self.__window.read()
            if event == "Voltar" or event == sg.WIN_CLOSED:
                break
            elif event == "-BT_DADOS_USUARIO-":
                self.__window.hide()
                self.open_dados_usuario()
            elif event == "-BT_FINANCEIRO-":
                self.__controlador.calculo_financeiro()
        self.close()

    def tela_cadastro_usuario(self):
        sg.theme("DarkBrown")
        layout = [[sg.Text("CADASTRO DO USUARIO", size=(40, 2), font="Arial")],
                  [sg.Text("NOME", size=(15, 1)), sg.InputText(key="-IT_NOME-")],
                  [sg.Text("CPF", size=(15, 1)), sg.InputText(key="-IT_CPF-")],
                  [sg.Text("TELEFONE", size=(15,1)), sg.InputText(key="-IT_TELEFONE-")],
                  [sg.Text("NOME DE USUARIO", size=(15, 1)), sg.InputText(key="-IT_NOME_USUARIO-")],
                  [sg.Text("SENHA DE USUARIO", size=(15, 1)), sg.InputText(key="-IT_SENHA_USUARIO-")],
                  [sg.Text("TEMPO DA CONSULTA", size=(15, 1)), sg.InputText(key="-IT_TEMPO-")],
                  [sg.Text("PREÇO DA CONSULTA", size=(15, 1)), sg.InputText(key="-IT_PRECO-")],
                  [sg.Frame(layout=[
                      [sg.Radio("M", "RADIO1", size=(10, 1), key="it_masc"),
                       sg.Radio("F", "RADIO1", size=(10, 1), key="it_fem")]],
                      title="Sexo", relief=sg.RELIEF_SUNKEN, )],
                  [sg.Submit("Finalizar cadastro"), sg.Button("Voltar")]
                  ]
        self.__window = sg.Window("Cadastro Usuario").Layout(layout)

    def open_tela_cadastro_usuario(self):
        self.tela_cadastro_usuario()
        while True:
            event, value = self.__window.read()
            if event == "Voltar" or event == sg.WIN_CLOSED:
                break
            elif event == "Finalizar cadastro":
                if not (value["-IT_NOME-"].replace(" ", "")).isalpha():
                    self.mostra_mensagem("Atencao", "FORMATO DE NOME INVALIDO")
                else:
                    cpf = CPF()
                    if not cpf.validate(cpf.mask(value["-IT_CPF-"])):
                        self.mostra_mensagem("Atencao", "CPF NÃO EXISTE")
                    else:
                        if len(value["-IT_TELEFONE-"]) != 11:
                            self.mostra_mensagem("Atencao", "FORMATO DE TELEFONE INVALIDO")
                        else:
                            if value["it_masc"]:
                                sexo = "M"
                            else:
                                sexo = "F"
                                if (value["-IT_NOME_USUARIO-"].isalpha() is False or len(value["-IT_NOME_USUARIO-"])< 8
                                        or len(value["-IT_NOME_USUARIO-"]) > 20):
                                    self.mostra_mensagem("Atencao", "NOME DE USUARIO INVALIDO")
                                else:
                                    if (value["-IT_SENHA_USUARIO-"].isalnum() is False
                                            or value["-IT_SENHA_USUARIO-"].isdigit() is True
                                            or value["-IT_SENHA_USUARIO-"].isalpha()
                                            or len(value["-IT_SENHA_USUARIO-"]) < 8
                                            or len(value["-IT_SENHA_USUARIO-"]) > 16):
                                        self.mostra_mensagem("Atencao", "SENHA DE USUARIO INVALIDA")
                                    else:
                                        if int(value["-IT_TEMPO-"]) < 10 or int(value["-IT_TEMPO-"]) > 60:
                                            self.mostra_mensagem("Atencao", "TEMPO DE CONSULTA INVALIDO")
                                        else:
                                            if not (float(value["-IT_PRECO-"]) > 0):
                                                self.mostra_mensagem("Atencao", "PRECO DA CONSULTA INVALIDO")

                            self.__controlador.cadastro_usuario({"nome": value["-IT_NOME-"], "cpf": value["-IT_CPF-"],
                                                                 "telefone": value["-IT_TELEFONE-"], "sexo": sexo,
                                                                 "nome_usuario": value["-IT_NOME_USUARIO-"],
                                                                 "senha_usuario": value["-IT_SENHA_USUARIO-"],
                                                                 "tempo_consulta": int(value["-IT_TEMPO-"]),
                                                                 "preco_consulta": int(value["-IT_PRECO-"])})
                            break
        self.close()

    def dados_usuario(self, dados_usuario):
        cpf = CPF()
        layout = [[sg.Text(f'NOME:{dados_usuario["nome"]}', size=(40, 1), font="Arial")],
                  [sg.Text(f'CPF: {cpf.mask(dados_usuario["cpf"])}', size=(40, 1), font="Arial")],
                  [sg.Text(f'TELEFONE: {dados_usuario["telefone"]}', size=(40, 1), font="Arial")],
                  [sg.Text(f'SEXO: {dados_usuario["sexo"]}', size=(40, 1), font="Arial")],
                  [sg.Text(f'PREÇO DA CONSULTA: {dados_usuario["preco"]}', size=(40, 1), font="Arial")],
                  [sg.Button("Voltar"), sg.Button("Alterar Usuario")]
                  ]
        self.__window = sg.Window("Menu Clientes").Layout(layout)

    def open_dados_usuario(self):
        dados_usuario = self.__controlador.pega_dados_usuario()
        self.dados_usuario(dados_usuario)
        while True:
            event, value = self.__window.read()
            if event == "Voltar" or event == sg.WIN_CLOSED:
                break
            elif event == "Alterar Usuario":
                self.open_altera_dados_usuario(dados_usuario)

    def tela_altera_dados_usuario(self, dados_usuario):
        sg.theme("DarkBrown")
        if dados_usuario["sexo"] == "M":
            frame_layout = [
                [sg.Radio("M", "RADIO1", size=(10, 1), key="it_masc", default=True),
                 sg.Radio("F", "RADIO1", size=(10, 1), key="it_fem")]]
        else:
            frame_layout = [
                [sg.Radio("M", "RADIO1", size=(10, 1), key="it_masc"),
                 sg.Radio("F", "RADIO1", size=(10, 1), key="it_fem", default=True)]]
        layout = [[sg.Text("CADASTRO DO USUARIO", size=(40, 2), font="Arial")],
                  [sg.Text("NOME", size=(15, 1)),
                   sg.InputText(f'{dados_usuario["nome"]}', key="-IT_NOME-")],
                  [sg.Text("CPF", size=(15, 1)),
                   sg.Text(f'{dados_usuario["cpf"]}')],
                  [sg.Text("TELEFONE", size=(15, 1)),
                   sg.InputText(f'{dados_usuario["telefone"]}', key="-IT_TELEFONE-")],
                  [sg.Text("NOME DE USUARIO", size=(15, 1)),
                   sg.InputText(f'{dados_usuario["nome_usuario"]}', key="-IT_NOME_USUARIO-")],
                  [sg.Text("SENHA DE USUARIO", size=(15, 1)),
                   sg.InputText(f'{dados_usuario["senha_usuario"]}', key="-IT_SENHA_USUARIO-")],
                  [sg.Text("PREÇO DA CONSULTA", size=(15, 1)),
                   sg.InputText(f'{dados_usuario["preco"]}', key="-IT_PRECO-")],
                  [sg.Frame(layout=frame_layout, title="Sexo", relief=sg.RELIEF_SUNKEN)],
                  [sg.Submit("Alterar Dados"), sg.Button("Voltar")]
                  ]
        self.__window = sg.Window("Alterar Dados Usuario").Layout(layout)

    def open_altera_dados_usuario(self, dados_usuario):
        self.tela_altera_dados_usuario(dados_usuario)
        while True:
            event, value = self.__window.read()
            if event == "Voltar" or event == sg.WIN_CLOSED:
                break
            elif event == "Alterar Dados":
                if not (value["-IT_NOME-"].replace(" ", "")).isalpha():
                    self.mostra_mensagem("Atencao", "FORMATO DE NOME INVALIDO")
                else:
                    if len(value["-IT_TELEFONE-"]) != 11:
                        self.mostra_mensagem("Atencao", "FORMATO DE TELEFONE INVALIDO")
                    else:
                        if value["it_masc"]:
                            sexo = "M"
                        else:
                            sexo = "F"
                            if (value["-IT_NOME_USUARIO-"].isalpha() is False or len(value["-IT_NOME_USUARIO-"])< 8
                                    or len(value["-IT_NOME_USUARIO-"]) > 20):
                                self.mostra_mensagem("Atencao", "NOME DE USUARIO INVALIDO")
                            else:
                                if (value["-IT_SENHA_USUARIO-"].isalnum() is False
                                        or value["-IT_SENHA_USUARIO-"].isdigit() is True
                                        or value["-IT_SENHA_USUARIO-"].isalpha()
                                        or len(value["-IT_SENHA_USUARIO-"]) < 8
                                        or len(value["-IT_SENHA_USUARIO-"]) > 16):
                                    self.mostra_mensagem("Atencao", "SENHA DE USUARIO INVALIDA")
                                else:
                                    if not (float(value["-IT_PRECO-"]) > 0):
                                        self.mostra_mensagem("Atencao", "PRECO DA CONSULTA INVALIDO")

                    self.__controlador.alterar_usuario({"nome": value["-IT_NOME-"],
                                                         "telefone": value["-IT_TELEFONE-"], "sexo": sexo,
                                                         "nome_usuario": value["-IT_NOME_USUARIO-"],
                                                         "senha_usuario": value["-IT_SENHA_USUARIO-"],
                                                         "preco_consulta": int(value["-IT_PRECO-"])})
                    break
        self.close()

    def close(self):
        self.__window.close()

    def mostra_mensagem(self, titulo: str, mensagem: str):
        sg.Popup(titulo, mensagem)
