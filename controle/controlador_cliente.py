from entidade.cliente import Cliente
from limite.tela_cliente import TelaCliente


class ControladorClientes:
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__clientes = []
        self.__tela_clientes = TelaCliente(self)

    @property
    def clientes(self):
        return self.__clientes

    def numero_clientes(self):
        numero_clientes = len(self.__clientes)
        return numero_clientes

    def adicionar_no_historico(self, consulta, usuario):
        observacao = self.__tela_clientes.pega_observacao()
        consulta.cliente.historico.append(f"{consulta.data} | {consulta.horario} | {usuario.preco_consulta} | {usuario.nome} | {observacao} ")
        return f"{consulta.data} | {consulta.horario} | {usuario.preco_consulta} | {usuario.nome} | {observacao} "

    def pega_cliente_por_cpf(self):
        cpf_cliente = self.__tela_clientes.seleciona_cliente()
        for cliente in self.__clientes:
            if cliente.cpf == cpf_cliente:
                return cliente
        return "CPF NAO CADASTRADO"

    def incluir_cliente(self):
        dados_cliente = self.__tela_clientes.pega_dados_cliente()
        for cliente in self.__clientes:
            if dados_cliente["cpf"] == cliente.cpf:
                self.__tela_clientes.mostra_mensagem("!!!! CPF JÁ CADASTRADO !!!!")
                return None
        cliente = Cliente(dados_cliente["nome"], dados_cliente["cpf"],
                          dados_cliente["telefone"], dados_cliente["sexo"])
        for var, att in cliente.__dict__.items():
            if att is None:
                self.__tela_clientes.mostra_mensagem(f"VALOR DE {var.upper()} INVÁLIDO")
                del cliente
                return None
        self.__clientes.append(cliente)
        self.__tela_clientes.mostra_mensagem(f"{cliente} cadastrado com sucesso!")
        input()

    def lista_clientes(self):
        self.__tela_clientes.mostra_mensagem("****** LISTA DE CLIENTES ******")
        for cliente in self.__clientes:
            self.__tela_clientes.mostra_cliente({"nome": cliente.nome, "cpf": cliente.cpf,
                                                 "telefone": cliente.telefone, "sexo": cliente.sexo})
        input()

    def altera_cliente(self):
        self.lista_clientes()
        cliente = self.pega_cliente_por_cpf()
        if cliente is not str and isinstance(cliente, Cliente):
            valores = {1: "nome", 2: "cpf", 3: "telefone", 4: "sexo", 0: 0}
            valores_lista = ["1 - Nome", "2 - CPF", "3 - Telefone", "4 - Sexo", "0 - Voltar"]
            for valor in valores_lista:
                self.__tela_clientes.mostra_mensagem(valor)
            while True:
                valor_escolhido = self.__tela_clientes.pega_valor()
                valor = valores[valor_escolhido]
                print(valor)
                if not isinstance(valor, str):
                    break
                novo_valor = self.__tela_clientes.pega_novo_valor()
                cliente.atualiza_atributo(valor, novo_valor)
                if cliente.nome != novo_valor and valor_escolhido == 1:
                    self.__tela_clientes.mostra_mensagem("Valor invalido, somente letras")
                elif cliente.cpf != novo_valor and valor_escolhido == 2:
                    self.__tela_clientes.mostra_mensagem("Valor invalido, somente numeros")
                elif cliente.telefone != novo_valor and valor_escolhido == 3:
                    self.__tela_clientes.mostra_mensagem("Valor invalido, somente somente numeros")
                elif cliente.sexo != novo_valor and valor_escolhido == 4:
                    self.__tela_clientes.mostra_mensagem("Valor invalido, somente m ou f")
                else:
                    self.__tela_clientes.mostra_mensagem(cliente.nome + " Alteracao feita com sucesso")
                input()

    def exclui_cliente(self):
        self.lista_clientes()
        cliente = self.pega_cliente_por_cpf()
        autenticacao = self.__controlador_principal.controlador_consulta.pega_codigo_por_cliente(cliente)
        if autenticacao is str:
            if cliente is not str:
                self.__clientes.remove(cliente)
                self.__tela_clientes.mostra_mensagem(f"{cliente} removido com sucesso")
            else:
                self.__tela_clientes.mostra_mensagem("!!!! CPF NÃO CADASTRADO !!!!")
        else:
            self.__tela_clientes.mostra_mensagem("Ha consultas marcadas com esse cliente")

    def mostra_historico_cliente(self):
        self.lista_clientes()
        cliente = self.pega_cliente_por_cpf()
        if cliente is not str:
            self.__tela_clientes.mostra_mensagem(cliente.historico)
        else:
            self.__tela_clientes.mostra_mensagem(cliente)
        input()

    def mostra_menu_clientes(self):
        lista_opcoes = {1: self.incluir_cliente, 2: self.lista_clientes, 3: self.altera_cliente,
                        4: self.exclui_cliente, 5: self.mostra_historico_cliente, 0: 0}
        while True:
            opcao = self.__tela_clientes.lista_opcoes()
            if opcao == 0:
                break
            try:
                funcao = lista_opcoes[opcao]
                funcao()
            except ValueError:
                self.__tela_clientes.mostra_mensagem("OPÇÃO INVALIDA")
