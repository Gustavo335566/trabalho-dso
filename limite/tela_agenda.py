

class Tela_Agenda:
    def Tela_Menu(self):
        print("----Agenda-----")
        print("1 - excluir consulta")
        print("2 - Imprimir agenda")
        print("3 - Procurar Consulta")
        print("0 - para sair")
        opcao = int(input("opcao: "))
        lista = [1, 2, 3, 0]
        while opcao not in lista:
            print("Valor incorreto")
            opcao = int(input("opcao: "))
        return opcao

    def imprimir(self, k, v):
        print("-------Minhas consultas------")
        print(k, v)

    def inclui(self, mensagem):
        print(mensagem)

    def exclui(self, mensagem):
        print(mensagem)

    def pega_cpf_cliente(self):
        cpf = str(input("Digite aqui o seu cpf: "))
        while True(len(cpf) != 11):
            print("Digito invlaido somente numeros")
            cpf = str(input("Digite aqui o seu cpf: "))
        return cpf

    def imprimir_consulta(self, consulta):
        print(consulta)

