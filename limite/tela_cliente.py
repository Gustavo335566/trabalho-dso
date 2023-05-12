

class TelaCliente:
    def __init__(self, controlador):
        self.__controlador = controlador

    def pega_dados_cliente(self):
        print("****** CADASTRO CLIENTE ******")
        while True:
            nome = input("Nome: ").title()
            nome_comprimido = nome.replace(" ", "")
            if nome_comprimido.isalpha():
                break
        cpf = input("CPF: ")
        telefone = input("Telefone: ")
        sexo = input("Sexo [M/F]: ")
        return {"nome": nome, "cpf": cpf, "telefone": telefone, "sexo": sexo}

    def pega_valor(self):
        print("*" * 30)
        print("******** ALTERAR CLIENTE ********")
        print("*" * 30)
        print("1 - Nome")
        print("2 - CPF")
        print("3 - Telefone")
        print("4 - Sexo")
        print("0 - Voltar")
        try:
            valor = int(input("Qual valor será alterado? "))
            return valor
        except ValueError:
            print("Escolha um valor dentre as opções")

    def pega_novo_valor(self):
        novo = input("Novo valor: ")
        return novo

    def mostra_cliente(self, dados_cliente):
        print("-="*30)
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
        try:
            opcao = int(input("Opção: "))
            return opcao
        except ValueError:
            print("Escolha um valor dentre as opções")


    def seleciona_cliente(self):
        cpf = input("CPF do cliente: ")
        return cpf

    def mostra_mensagem(self, msg):
        print(msg)
