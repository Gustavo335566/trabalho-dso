from entidade.consulta import Consulta
from controle.controlador_cliente import ControladorClientes
from limite.tela_consulta import TelaConsulta


class ControladorConsulta:
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__historico_consultas = []
        self.__tela_consulta = TelaConsulta(self)
        #ADICIONAR CONSULTA AO HISTORICO

    def pega_codigo_por_cliente(self, cliente):
        for consulta in self.__historico_consultas:
            if consulta.cliente == cliente:
                return consulta.codigo
        return "CLIENTE NAO POSSUI CONSULTA"

    def pega_consulta_por_codigo(self, codigo):
        for consulta in self.__historico_consultas:
            if consulta.codigo == codigo:
                return consulta
        return "CONSULTA NAO EXISTENTE"

    def cadastrar_consulta(self, usuario):
        existe_cliente = False
        existe = False
        dados_consulta = self.__tela_consulta.pega_dados_consulta(self.__controlador_principal.controlador_cliente.pega_cliente_por_cpf())
        for cl in self.__controlador_principal.controlador_cliente.clientes:
            if dados_consulta["cliente"] == cl:
                existe_cliente = True
        if existe_cliente:
            for consulta in self.__historico_consultas:
                if dados_consulta["data"] is not None:
                    existe = True
            if existe:
                self.__tela_consulta.mostra_mensagem("!!!!! HORÁRIO INDISPONÍVEL !!!!!")
            else:
                consulta = Consulta(dados_consulta["cliente"], dados_consulta["codigo"], dados_consulta["data"], dados_consulta["horario"])
                self.__historico_consultas.append(consulta)
                self.__controlador_principal.controlador_cliente.adicionar_no_historico(consulta, usuario)
                return consulta

    def lista_consultas(self, usuario):
        for consulta in self.__historico_consultas:
            self.__tela_consulta.mostra_dados_consulta({"codigo": consulta.codigo,
                                                        "cliente": consulta.cliente,
                                                        "data": consulta.data})

    def exclui_consulta(self, usuario):
        self.lista_consultas(usuario)
        codigo = self.__tela_consulta.seleciona_consulta()
        consulta = self.pega_consulta_por_codigo(codigo)
        if consulta is not None:
            self.__historico_consultas.append(f"{consulta} removido com sucesso")
            self.__tela_consulta.mostra_mensagem(f"{consulta} removido com sucesso")
            return consulta
        else:
            return "!!!! CONSULTA NÃO CADASTRADA !!!!"

    def finalizar_consulta(self, usuario):
        self.lista_consultas(usuario)
        codigo = self.__tela_consulta.seleciona_consulta()
        consulta = self.pega_consulta_por_codigo(codigo)

    def retornar(self):
        pass

    def mostra_menu_consulta(self, usuario):
        lista_opcoes = {1: self.cadastrar_consulta, 2: self.lista_consultas, 4: self.exclui_consulta, 0: self.retornar}
        while True:
            opcao = self.__tela_consulta.lista_opcoes()
            funcao = lista_opcoes[opcao]
            if opcao == 0:
                break
            else:
                funcao(usuario)

#TERMINAR CONSULTA URGENTE: TERMINAR DIAGRAMA, ALTERAR ATRIBUIÇÕES.