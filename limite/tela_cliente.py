

class TelaCliente:
    def __init__(self, controlador):
        self.__controlador = controlador

    def pega_dados_cliente(self):
        print("****** CADASTRO CLIENTE ******")
        id_cliente = input("ID: ")
        nome = input("Nome: ")
        cpf = input("CPF: ")
        telefone = input("Telefone: ")
        sexo = input("Sexo [M/F]: ")
        return {"id_cliente": id_cliente, "nome": nome, "cpf": cpf, "telefone": telefone, "sexo": sexo}

    def mostra_cliente(self, dados_cliente):
        print("-="*30)
        print("ID:", dados_cliente["id_cliente"], end=" | ")
        print("NOME:", dados_cliente["nome"], end=" | ")
        print("CPF:", dados_cliente["cpf"], end=" | ")
        print("TELEFONE:", dados_cliente["telefone"], end=" | ")
        print("SEXO:", dados_cliente["sexo"])


    def lista_opcoes(self):
        print("*"*30)
        print("******** MENU CLIENTES ********")
        print("*"*30)
        print("1 - Cadastrar Cliente")
        print("2 - Listar Clientes")
        print("3 - Alterar Cliente")
        print("4 - Excluir Cliente")
        print("0 - Voltar")
        opcao = int(input("Opção: "))
        return opcao

    def seleciona_cliente(self):
        cpf = input("CPF do cliente: ")
        return cpf

    def mostra_mensagem(self, msg):
        print(msg)
