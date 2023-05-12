from entidade.consulta import Consulta
from controle.controlador_cliente import ControladorClientes
from limite.tela_consulta import TelaConsulta


class ControladorConsulta:
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__consultas = []
        self.__tela_consulta = TelaConsulta(self)
        #ADICIONAR CONSULTA AO HISTORICO

    def pega_codigo_por_cliente(self, cliente):
        for consulta in self.__consultas:
            if consulta.cliente == cliente:
                return consulta.codigo
        return "CLIENTE NAO POSSUI CONSULTA"

    def pega_consulta_por_codigo(self, codigo: int):
        for consulta in self.__consultas:
            if consulta.codigo == codigo:
                return consulta
        return "CONSULTA NAO EXISTENTE"

    def cadastrar_consulta(self):
        existe_cliente = False
        existe = False
        dados_consulta = self.__tela_consulta.pega_dados_consulta()
        cliente = ControladorClientes.pega_cliente_por_cpf(self.__controlador_principal.controlador_cliente, dados_consulta["cpf"])
        for cl in self.__controlador_principal.controlador_cliente.clientes:
            if cliente == cl:
                existe_cliente = True
            print(cliente)
        if existe_cliente:
            for consulta in self.__consultas:
                if dados_consulta["data"] is not None:
                    existe = True
            if existe:
                self.__tela_consulta.mostra_mensagem("!!!!! HORÁRIO INDISPONÍVEL !!!!!")
            else:
                consulta = Consulta( cliente, dados_consulta["codigo"], dados_consulta["data"], dados_consulta["horario"])
                self.__consultas.append(consulta)

    def lista_consultas(self):
        for consulta in self.__consultas:
            TelaConsulta.mostra_dados_consulta(TelaConsulta(self), {"codigo": consulta.codigo,
                                                                    "cliente": consulta.cliente,
                                                                    "data": consulta.data})

    def exclui_consulta(self):
        self.lista_consultas()
        codigo_consulta = self.__tela_consulta.seleciona_consulta()
        consulta = self.pega_consulta_por_codigo(codigo_consulta)
        if consulta is not None:
            self.__consultas.remove(consulta)
            self.__tela_consulta.mostra_mensagem(f"{consulta} removido com sucesso")
        else:
            self.__tela_consulta.mostra_mensagem("!!!! CONSULTA NÃO CADASTRADA !!!!")

    def retornar(self):
        self.__controlador_principal.abre_tela()

    def mostra_menu_consulta(self):
        lista_opcoes = {1: self.cadastrar_consulta, 2: self.lista_consultas, 4: self.exclui_consulta, 0: self.retornar}
        while True:
            opcao = self.__tela_consulta.lista_opcoes()
            funcao = lista_opcoes[opcao]
            funcao()

#TERMINAR CONSULTA URGENTE: TERMINAR DIAGRAMA, ALTERAR ATRIBUIÇÕES.