

class Tela_usuario:
    def tela_opcoes(self):
        print("------USUARIO--------")
        print("Escolha a opcao")
        print("1 - Cadastrar Cliente")
        print("2 - Fazer uma Consulta")
        print("3 - Adicionar a historico medico")
        print("4 - Alterar dados do Cliente")
        print("5 - Excluir Cliente")
        print("6 - Excluir Consulta")
        print("7 - Excluir do historico medico")
        print("8 - Listar Clientes")
        print("9 - Listar Minhas Consultas")
        print("10 - Historico de consultas")
        print("0 - Voltar para a tela principal")
        opcao = int(input("Escolha a opcao: "))
        return opcao
