from entidade.consulta import Consulta
from controle.controlador_cliente import ControladorClientes
from limite.tela_consulta import TelaConsulta


class ControladorConsulta:
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__historico_consultas = []
        self.__todas_consultas = []
        self.__tela_consulta = TelaConsulta(self)
        self.__contador_codigo = 1000
        #ADICIONAR CONSULTA AO HISTORICO

    @property
    def contador_codigo(self):
        return self.__contador_codigo

    @property
    def todas_consultas(self):
        return self.__todas_consultas

    def add_consulta(self, consulta):
        self.__todas_consultas.append(consulta)

    def pega_codigo_por_cliente(self, cliente):
        for consulta in self.__todas_consultas:
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
        existe = True
        self.__contador_codigo += 1
        codigo = self.__contador_codigo
        dados_consulta = self.__tela_consulta.pega_dados_consulta(self.__controlador_principal.controlador_cliente.pega_cliente_por_cpf())
        for cl in self.__controlador_principal.controlador_cliente.clientes:
            if dados_consulta["cliente"] == cl:
                existe_cliente = True
        if existe_cliente:
            for data, horarios in usuario.agenda.minhas_consultas.items():
                for hora, valor in horarios.items():
                    if(data == dados_consulta["data"]):
                        if(hora == dados_consulta["horario"] and valor == "vago"):
                            existe = False
            if existe:
                self.__tela_consulta.mostra_mensagem("!!!!! HORÁRIO INDISPONÍVEL !!!!!")
            else:
                consulta = Consulta(dados_consulta["cliente"], codigo, dados_consulta["data"], dados_consulta["horario"])
                self.__historico_consultas.append(consulta)
                self.__controlador_principal.controlador_cliente.adicionar_no_historico(consulta, usuario)
                return consulta

    def lista_consultas(self):
        for consulta in self.__historico_consultas:
            self.__tela_consulta.mostra_dados_consulta({"codigo": consulta.codigo,
                                                        "cliente": consulta.cliente,
                                                        "data": consulta.data})

    def exclui_consulta(self):
        self.lista_consultas()
        codigo = self.__tela_consulta.seleciona_consulta()
        consulta = self.pega_consulta_por_codigo(codigo)
        if consulta is not None:
            self.__historico_consultas.append(f"{consulta} removido com sucesso")
            self.__tela_consulta.mostra_mensagem(f"{consulta} removido com sucesso")
            self.__todas_consultas.remove(consulta)
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