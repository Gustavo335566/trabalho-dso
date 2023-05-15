

class TelaAgenda:
    def menu_agenda(self):
        print("----Agenda-----")
        print("1 - Cadastrar Consulta")
        print("2 - Excluir Consulta")
        print("3 - Imprimir Agenda")
        print("4 - Procurar Consulta")
        print("0 - Voltar")
        lista = [1, 2, 3, 4, 0]
        while True:
            opcao = input("Escolha a opcao: ")
            if opcao.isdigit():
                if int(opcao) in lista:
                    return int(opcao)
            print("Valor incorreto")

    def imprimir(self, hora, consulta):
        print(f"{hora} : {consulta}")

    def inclui(self, mensagem):
        print(mensagem)

    def exclui(self, mensagem):
        print(mensagem)

    def pega_cpf_cliente(self):
        cpf = str(input("Digite aqui o seu cpf: "))
        while len(cpf) != 11:
            print("Digito invalido somente numeros")
            cpf = str(input("Digite aqui o seu cpf: "))
        return cpf

    def imprimir_consulta(self, consulta):
        print(consulta)

    def mostra_mensagem(self, mensagem):
        print(mensagem)
