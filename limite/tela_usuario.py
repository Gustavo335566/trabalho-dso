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
                                        if value["-IT_TEMPO-"] < 10 or value["-IT_TEMPO-"] > 60:
                                            self.mostra_mensagem("Atencao", "TEMPO DE CONSULTA INVALIDO")
                                        else:
                                            if not (value["-IT_PRECO-"] > 0):
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

    def close(self):
        self.__window.close()

    def mostra_mensagem(self, titulo: str, mensagem: str):
        sg.Popup(titulo, mensagem)

    def mudanca_dados_usuario(self):
        print("Atencao digite apenas um dado de cada vez que voce queira alterar")
        print("1 - Telefone")
        print("2 - Preco da consulta")
        print("3 - Tempo da consulta")
        print("4 - Nome")
        print("5 - Nome de usuario")
        print("6 - Senha")
        print("7 - Sexo")
        print("0 - Sair")
        lista = [1, 2, 3, 4, 5, 6, 7, 0]
        while True:
            opcao = (input("Digite aqui o que voce quer mudar: "))
            if opcao.isdigit():
                if int(opcao) in lista:
                    return int(opcao)
            print("Valor incorreto")

    def pega_telefone(self):
        telefone = str(input("Digite o seu telefone no formato xx9xxxxxxxx: "))
        while telefone.isdigit() is False or len(telefone) != 11:
            print("Telefone inválido")
            telefone = str(input("Digite o seu telefone no formato xx9xxxxxxxx: "))
        return telefone

    def pega_tempo_consulta(self):
        tempo_consulta = int(input("Tempo de consulta: "))
        while 60 > tempo_consulta < 10:
            print("Tempo de consulta somente em minutos, de 10min a 60min")
            tempo_consulta = int(input("Tempo de consulta: "))
        return tempo_consulta

    def pega_senha_usuario(self):
        senha_usuario = str(input("Digite uma senha: "))
        while senha_usuario.isalnum() is False or senha_usuario.isdigit() is True or senha_usuario.isalpha() or len(
                senha_usuario) < 8 or len(senha_usuario) > 16:
            print("Senha deve ter letras e numeros, e ter de 8 a 16 caracteres")
            senha_usuario = str(input("digite uma senha: "))
        return senha_usuario

    def pega_nome(self):
        nome_completo = str(input("Digite o seu nome: ")).capitalize()
        nome = nome_completo.replace(" ", "")
        while nome.isalpha() is False:
            print("O nome so pode conter letras")
            nome_completo = str(input("Digite o seu nome: "))
            nome = nome_completo.replace(" ", "")
        return nome_completo

    def pega_nome_usuario(self):
        nome_usuario = str(input("Digite o seu nome de usuario: "))
        while nome_usuario.isalpha() is False or len(nome_usuario) < 8 or len(nome_usuario) > 20:
            print("O nome de usuario deve possuir somente letras e tamanho de 8 a 20 caracteres")
            nome_usuario = str(input("Digite o seu nome de usuario: "))
        return nome_usuario

    def pega_preco(self):
        preco_consulta = float(input("Preco da consulta: "))
        while not preco_consulta > 0:
            print("Preco invalido")
            preco_consulta = float(input("Preco da consulta: "))
        return preco_consulta

    def pega_cpf_usuario(self):
        cpf = str(input("Digite o seu cpf: "))
        while cpf.isdigit() is False or len(cpf) != 11:
            print("CPF inválido")
            cpf = input("Digite o seu cpf: ")
        return cpf

    def pega_sexo(self):
        sexo = str(input("Digite o seu sexo [m/f]: ")).upper()
        while sexo != "M" and sexo != "F":
            print("Somente M ou F")
            sexo = str(input("Digite o seu sexo [m/f]: ")).upper()
        return sexo

    def palavra_chave(self):
        palavra = str(input("Digite a palavra chave: "))
        return palavra
