

class TelaConsulta:
    def __init__(self, controlador):
        self.__controlador = controlador

    def pega_dados_consulta(self, cliente, usuario):
        print("******** DADOS DA CONSULTA ********")
        datas_consulta = {1: "Segunda", 2: "Terça", 3: "Quarta", 4: "Quinta", 5: "Sexta"}
        print("1: Segunda\n2: Terça\n3: Quarta\n4: Quinta\n5: Sexta")
        while True:
            data = input("Data da Consulta: ")
            if data.isdigit():
                data = int(data)
                if data in datas_consulta.keys():
                    break
            print("Valor incorreto")
        while True:
            horario = input("Horario Consulta [x:xx]: ")
            if horario in usuario.agenda.minhas_consultas[datas_consulta[data]].keys():
                break
            print("Horario nao consta na agenda, coloque outro valor")
        return {"cliente": cliente, "data": datas_consulta[data], "horario": horario}

    def mostra_dados_consulta(self, dados_consulta: dict):
        print("CÓD:", dados_consulta["codigo"], end=" | ")
        print("Nome:", dados_consulta["cliente"].nome, end=" | ")
        print("CPF:", dados_consulta["cliente"].cpf, end=" | ")
        print("DATA:", dados_consulta["data"])
        print("\n")

    def seleciona_consulta(self):
        codigo = int(input("Código da consulta que deseja selecionar: "))
        return codigo

    def mostra_mensagem(self, msg):
        print(msg)
