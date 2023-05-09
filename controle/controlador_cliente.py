from entidade.cliente import Cliente
from limite.tela_cliente import TelaCliente
from controle.validate_dados import *


class ControladorClientes:
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__clientes = [Cliente("nome", "13539399950", "4832858585", "M")]
        self.__tela_clientes = TelaCliente(self)

    @property
    def clientes(self):
        return self.__clientes

    def pega_cliente_por_cpf(self, cpf: str):
        for cliente in self.__clientes:
            if cliente.cpf == cpf:
                return cliente
        return None

    def incluir_cliente(self):
        dados_cliente = self.__tela_clientes.pega_dados_cliente()
        for cliente in self.__clientes:
            if dados_cliente["cpf"] == cliente.cpf:
                self.__tela_clientes.mostra_mensagem("!!!! CPF JÁ CADASTRADO !!!!")
                return None
        cliente = Cliente(dados_cliente["nome"], dados_cliente["cpf"],
                          dados_cliente["telefone"], dados_cliente["sexo"])
        print(cliente.__dict__)
        for var, att in cliente.__dict__.items():
            if att is None:
                self.__tela_clientes.mostra_mensagem(f"VALOR DE {var.upper()} INVÁLIDO")
                del cliente
                return None
        self.__clientes.append(cliente)
        self.__tela_clientes.mostra_mensagem(f"{cliente} cadastrado com sucesso!")

    def lista_clientes(self):
        for cliente in self.__clientes:
            self.__tela_clientes.mostra_cliente({"nome": cliente.nome, "cpf": cliente.cpf,
                                                 "telefone": cliente.telefone, "sexo": cliente.sexo})

    def altera_cliente(self):
        self.lista_clientes()
        cpf_cliente = self.__tela_clientes.seleciona_cliente()
        cliente = self.pega_cliente_por_cpf(cpf_cliente)

        if cliente is not None and isinstance(cliente, Cliente):
            valores = {"nome": cliente.nome, "cpf": cliente.cpf, "telefone": cliente.telefone, "sexo": cliente.sexo, 0: self.retornar}
            valores_lista = list(valores.keys())
            print(valores_lista)

            for key, value in valores:
                valor = self.__tela_clientes.pega_valor()
                if valor == 0:
                    value()
                elif valor == valores_lista.index(value):
                    self.__tela_clientes.mostra_mensagem(key)
                    cliente.key = self.__tela_clientes.pega_novo_valor()
                self.__tela_clientes.mostra_mensagem(cliente.nome)
                #USAR WHILE, {"nome": nome}, settar valor


    def exclui_cliente(self):
        self.lista_clientes()
        cpf_cliente = self.__tela_clientes.seleciona_cliente()
        cliente = self.pega_cliente_por_cpf(cpf_cliente)

        if cliente is not None:
            self.__clientes.remove(cliente)
            self.__tela_clientes.mostra_mensagem(f"{cliente} removido com sucesso")
        else:
            self.__tela_clientes.mostra_mensagem("!!!! CPF NÃO CADASTRADO !!!!")

    def retornar(self):
        self.__controlador_principal.abre_tela()

    def mostra_menu_clientes(self):
        lista_opcoes = {1: self.incluir_cliente, 2: self.lista_clientes, 3: self.altera_cliente,
                        4: self.exclui_cliente, 0: self.retornar}
        while True:
            opcao = self.__tela_clientes.lista_opcoes()
            try:
                funcao = lista_opcoes[opcao]
                funcao()
            except ValueError:
                self.__tela_clientes.mostra_mensagem("OPÇÃO INVALIDA")
