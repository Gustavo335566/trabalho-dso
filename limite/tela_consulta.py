

class TelaConsulta:
    def __init__(self, controlador):
        self.__controlador = controlador

    def pega_dados_consulta(self):
        print("******** DADOS DA CONSULTA ********")
        codigo = 1000
        cpf = input("CPF do Cliente: ")
        data = input("Data da Consulta")
        horario = input("Horario Consulta")
        codigo += 1
        return {"codigo": codigo, "cpf": cpf, "data": data, "horario": horario}


    def mostra_dados_consulta(self, dados_consulta: dict):
        print("CÓD:", dados_consulta["codigo"], end=" | ")
        print("Nome:", dados_consulta["cliente"].nome, end=" | ")
        print("CPF:", dados_consulta["cliente"].cpf, end=" | ")
        print("DATA:", dados_consulta["data"])
        print("\n")

    def seleciona_consulta(self):
        codigo = int(input("Código da consulta que deseja selecionar: "))
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
