

class TelaPrincipal:
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal

    def lista_opcoes(self):
        print("*"*30)
        print("******* SISTEMA MÉDICO *******")
        print("*"*30)
        print("1 - Clientes")
        print("2 - Consultas")
        print("0 - Sair")
        opcao = int(input("Opção: "))
        return opcao
