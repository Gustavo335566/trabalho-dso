from entidade.cliente import Cliente
from limite.tela_cliente import TelaCliente
from persistencia.cliente_dao import ClienteDAO
import PySimpleGUI as sg
from excecoes.cliente_possui_consultas_exception import ClientePossuiConsultasException


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

    def alterar_cliente(self, dados_cliente):
        cliente = self.pega_cliente_por_cpf(dados_cliente["cpf"])
        if isinstance(cliente, Cliente):
            cliente.nome = dados_cliente["nome"]
            cliente.sexo = dados_cliente["sexo"]
            cliente.telefone = dados_cliente["telefone"]
            self.cliente_dao.add(cliente.cpf, cliente)

    def exclui_cliente(self, cpf_cliente):
        cliente = self.pega_cliente_por_cpf(cpf_cliente)
        autenticacao = self.__controlador_principal.controlador_consulta.verifica_se_tem_consulta(cliente)
        try:
            if not autenticacao:
                self.__cliente_dao.remove(cliente.cpf)
                self.__tela_clientes.mostra_mensagem("Cliente Removido", f"{cliente} removido com sucesso")
            else:
                raise ClientePossuiConsultasException("Cliente possui consultas")
        except ClientePossuiConsultasException as cpce:
            print(cpce)
            self.__tela_clientes.mostra_mensagem("Atencao", cpce)

    def abrir_tela(self):
        self.__tela_clientes.open()

    @property
    def tela_clientes(self):
        return self.__tela_clientes

    @property
    def cliente_dao(self):
        return self.__cliente_dao
