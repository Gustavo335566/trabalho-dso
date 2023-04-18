

class TelaConsulta:
    def __init__(self, controlador):
        self.__controlador = controlador

    def pega_dados_consulta(self):
        print("******** DADOS DA CONSULTA ********")
        codigo = input("Código da Consulta")
        cpf = input("CPF do Cliente: ")
        data = input("Data da Consulta")

        return {"codigo": codigo, "cpf": cpf, "data": data}

    def mostra_dados_consulta(self, dados_consulta: dict):
        print("Código da Consulta:", dados_consulta["codigo"])
        print("Cliente da Consulta:", dados_consulta["nome_cliente"])
        print("CPF do Cliente:", dados_consulta["cpf_cliente"])
        print("Data da Consulta:", dados_consulta["data"])
        print("\n")

    def seleciona_consulta(self):
        codigo = input("Código da consulta que deseja selecionar: ")
        return codigo

    def lista_opcoes(self):
        print("******* CONSULTAS *******")
        print("1 - Cadastrar Consulta")
        print("2 - Lista de Consultas")
        print("3 - Finalizar Consulta")
        print("4 - Remover Consulta")
        print("0 - Voltar")
        opcao = int(input("Opção: "))
        return opcao

    def mostra_mensagem(self, msg):
        print(msg)
