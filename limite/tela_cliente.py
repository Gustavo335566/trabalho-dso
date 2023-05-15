

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
            print("Nome invalido!")
        cpf = input("CPF: ")
        while len(cpf) != 11:
            print("CPF invalido!")
            cpf = input("CPF: ")
        telefone = input("Telefone [xx9xxxxxxxx]: ")
        while len(telefone) != 11:
            print("Telefone invalido!")
            telefone = input("Telefone [xx9xxxxxxxx]: ")
        sexo = input("Sexo [M/F]: ").upper()
        while sexo != "M" and sexo != "F":
            print("Sexo invalido!")
            sexo = input("Sexo [M/F]: ").upper()
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
        lista = [x for x in range(0, 5)]
        while True:
            valor = input("Digite a opcao: ")
            if valor.isdigit():
                if int(valor) in lista:
                    return int(valor)
            print("Valor incorreto")

    def pega_novo_valor(self):
        novo = input("Novo valor: ")
        return novo

    def pega_observacao(self):
        observacao = input("Observação: ")
        return observacao

    def mostra_cliente(self, dados_cliente):
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
        print("5 - Histórico Cliente")
        print("0 - Voltar")
        lista = [1, 2, 3, 4, 5, 0]
        while True:
            opcao = input("Escolha a opcao: ")
            if opcao.isdigit():
                if int(opcao) in lista:
                    return int(opcao)
            print("Valor incorreto")
            input()

    def seleciona_cliente(self):
        cpf = input("CPF do cliente: ")
        while len(cpf) != 11:
            print("CPF invalido")
            if cpf.isalnum():
                print("Falta digitos")
            else:
                print("Somente numeros")
            cpf = input("CPF do cliente: ")
        return cpf

    def mostra_mensagem(self, msg):
        print(msg)
