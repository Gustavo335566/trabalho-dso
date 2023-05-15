

class TelaPrincipal:
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal

    def lista_opcoes(self):
        print("*"*35)
        print("****** SISTEMA CADASTRO BABE ******")
        print("*"*35)
        print("1 - Login")
        print("2 - Cadastro")
        print("0 - Sair")
        lista = [0, 1, 2]
        while True:
            opcao = input("Opção: ")
            if opcao.isdigit():
                if int(opcao) in lista:
                    return int(opcao)
            print("Valor incorreto")

    def tela_login(self):
        nome_usuario = str(input("Coloque o seu nome de usuario: "))
        senha_usuario = str(input("Coloque a sua senha: "))
        return nome_usuario, senha_usuario

    def mostra_mensagem(self, mensagem: str):
        print(mensagem)
