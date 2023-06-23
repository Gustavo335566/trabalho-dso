from entidade.cliente import Cliente
from limite.tela_cliente import TelaCliente
from persistencia.cliente_dao import ClienteDAO
import PySimpleGUI as sg


class ControladorClientes:
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__cliente_dao = ClienteDAO()
        self.__tela_clientes = TelaCliente(self)

    def numero_clientes(self):
        lista_clientes = self.__cliente_dao.get_all()
        numero_clientes = len(lista_clientes)
        return numero_clientes

    def adicionar_no_historico(self, consulta, usuario):
        observacao = self.__tela_clientes.pega_observacao()
        consulta.cliente.historico.append(f"{consulta.data} | {consulta.horario} | {usuario.preco_consulta} | {usuario.nome} | {observacao} ")
        return f"{consulta.data} | {consulta.horario} | {usuario.preco_consulta} | {usuario.nome} | {observacao} "

    def pega_cliente_por_cpf(self, cpf_cliente):
        for cliente in self.__cliente_dao.get_all():
            if cliente.cpf == cpf_cliente:
                return cliente
        return False

    def pega_cpf_do_cliente(self, cliente):
        return cliente.cpf

    def busca_cliente(self, cpf_cliente):
        cliente = self.pega_cliente_por_cpf(cpf_cliente)
        if not cliente:
            self.__tela_clientes.mostra_mensagem("Atencao", "CPF NAO CADASTRADO")
        else:
            self.__tela_clientes.open_dados_cliente({"nome": cliente.nome, "cpf": cliente.cpf,
                                                     "telefone": cliente.telefone, "sexo": cliente.sexo})

    def incluir_cliente(self, dados_cliente):
        existe = False
        for cliente in self.__cliente_dao.get_all():
            if cliente.cpf == dados_cliente["cpf"]:
                existe = True
        if not existe:
            cliente = Cliente(dados_cliente["nome"], dados_cliente["cpf"],
                              dados_cliente["telefone"], dados_cliente["sexo"])
            self.__cliente_dao.add(cliente.cpf, cliente)
            self.__tela_clientes.mostra_mensagem("Cadastro Feito", f"{cliente} cadastrado com sucesso!")
        else:
            self.__tela_clientes.mostra_mensagem("Atencao", "CPF JA CADASTRADO NO SISTEMA")
        return None

    def listar_clientes(self):
        lista_botao = [[sg.Button(f'{cliente.cpf} {cliente.nome}',
                        key=cliente.cpf)] for cliente in self.__cliente_dao.get_all()]
        return lista_botao

    def altera_cliente(self):
        if len(self.__cliente_dao.get_all()) > 0:
            self.lista_clientes()
            cliente = self.pega_cliente_por_cpf()
            if cliente is not str and isinstance(cliente, Cliente):
                valores = {1: "nome", 2: "cpf", 3: "telefone", 4: "sexo", 0: 0}
                while True:
                    valor_escolhido = self.__tela_clientes.pega_valor()
                    valor = valores[valor_escolhido]
                    print(valor)
                    if not isinstance(valor, str):
                        break
                    novo_valor = self.__tela_clientes.pega_novo_valor()
                    cliente.atualiza_atributo(valor, novo_valor)
                    if (cliente.nome != novo_valor.title()) and valor_escolhido == 1:
                        print(cliente.nome, novo_valor)
                        self.__tela_clientes.mostra_mensagem("Valor invalido, somente letras")
                    elif cliente.cpf != novo_valor and valor_escolhido == 2:
                        self.__tela_clientes.mostra_mensagem("Valor invalido, somente numeros")
                    elif cliente.telefone != novo_valor and valor_escolhido == 3:
                        self.__tela_clientes.mostra_mensagem("Valor invalido, somente somente numeros")
                    elif cliente.sexo != novo_valor.upper() and valor_escolhido == 4:
                        self.__tela_clientes.mostra_mensagem("Valor invalido, somente m ou f")
                    else:
                        self.__tela_clientes.mostra_mensagem(cliente.nome + " Alteracao feita com sucesso")
        else:
            self.__tela_clientes.mostra_mensagem('não há clientes cadastrados')
        input()

    def exclui_cliente(self, cpf_cliente):
        cliente = self.pega_cliente_por_cpf(cpf_cliente)
        autenticacao = self.__controlador_principal.controlador_consulta.verifica_se_tem_consulta(cliente)
        if not autenticacao:
            if cliente is not str:
                self.__cliente_dao.remove(cliente.cpf)
                self.__tela_clientes.mostra_mensagem("Cliente Removido", f"{cliente} removido com sucesso")
        else:
            self.__tela_clientes.mostra_mensagem("Atencao", "Ha consultas marcadas com esse cliente")

    def mostra_historico_cliente(self):
        if len(self.clientes) > 0:
            self.lista_clientes()
            cliente = self.pega_cliente_por_cpf()
            if cliente is not str:
                self.__tela_clientes.mostra_mensagem(cliente.historico)
            else:
                self.__tela_clientes.mostra_mensagem(cliente)
        else:
            self.__tela_clientes.mostra_mensagem('não há clientes para se ver o historico')
        input()

    def abrir_tela(self):
        self.__tela_clientes.open()

    @property
    def tela_clientes(self):
        return self.__tela_clientes

    @property
    def cliente_dao(self):
        return self.__cliente_dao
