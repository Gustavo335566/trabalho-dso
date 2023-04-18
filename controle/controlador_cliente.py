from entidade.cliente import Cliente
from limite.tela_cliente import TelaCliente


class ControladorClientes:
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__clientes = []
        self.__tela_clientes = TelaCliente(self)

    def pega_cliente_por_cpf(self, cpf):
        for cliente in self.__clientes:
            if cliente.cpf == cpf:
                return cliente
            return None

    def incluir_cliente(self):
        existe = False
        dados_cliente = self.__tela_clientes.pega_dados_cliente()
        for cliente in self.__clientes:
            if dados_cliente["cpf"] == cliente.cpf:
                existe = True
        if existe:
            self.__tela_clientes.mostra_mensagem("!!!! CPF JÁ CADASTRADO !!!!")
        else:
            cliente = Cliente(dados_cliente["nome"], dados_cliente["cpf"],
                              dados_cliente["telefone"], dados_cliente["sexo"], dados_cliente["id_cliente"])
            self.__clientes.append(cliente)

    def lista_clientes(self):
        for cliente in self.__clientes:
            self.__tela_clientes.mostra_cliente({"id_cliente": cliente.id_cliente, "nome": cliente.nome,
                                                 "cpf": cliente.cpf, "telefone": cliente.telefone,
                                                 "sexo": cliente.sexo})

    def exclui_cliente(self):
        self.lista_clientes()
        cpf_cliente = self.__tela_clientes.seleciona_cliente()
        cliente = self.pega_cliente_por_cpf(cpf_cliente)

        if cliente is not None:
            self.__clientes.remove(cliente)
        else:
            self.__tela_clientes.mostra_mensagem("!!!! CPF NÃO CADASTRADO !!!!")

    def retornar(self):
        self.__controlador_principal.abre_tela()

    def mostra_menu_clientes(self):
        lista_opcoes = {1: self.incluir_cliente, 2: self.lista_clientes, 0: self.retornar}
        while True:
            opcao = self.__tela_clientes.lista_opcoes()
            funcao = lista_opcoes[opcao]
            funcao()
