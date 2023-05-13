

class TelaAgenda:
    def menu_agenda(self):
        print("----Agenda-----")
        print("1 - Cadastrar Consulta")
        print("2 - Excluir Consulta")
        print("3 - Imprimir Agenda")
        print("4 - Procurar Consulta")
        print("0 - Voltar")
        opcao = int(input("opcao: "))
        lista = [1, 2, 3, 4, 0]
        while opcao not in lista:
            print("Valor incorreto")
            opcao = int(input("opcao: "))
        return opcao

    def imprimir(self, k, v):
        print(f"{k} : {v}")

    def inclui(self, mensagem):
        print(mensagem)

    def exclui(self, mensagem):
        print(mensagem)

    def pega_cpf_cliente(self):
        cpf = str(input("Digite aqui o seu cpf: "))
        while True(len(cpf) != 11):
            print("Digito invalido somente numeros")
            cpf = str(input("Digite aqui o seu cpf: "))
        return cpf

    def imprimir_consulta(self, consulta):
        print(consulta)

    def mostra_mensagem(self, mensagem):
        print(mensagem)
