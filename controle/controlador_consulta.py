from entidade.consulta import Consulta
from limite.tela_consulta import TelaConsulta


class ControladorConsulta:
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__consultas = []
        self.__tela_consulta = TelaConsulta(self)

    def pega_consulta_por_codigo(self, codigo: int):
        for consulta in self.__consultas:
            if consulta.codigo == codigo:
                return consulta
        return None

    def cadastrar_consulta(self):
        existe = False
        dados_consulta = self.__tela_consulta.pega_dados_consulta()
        for consulta in self.__consultas:
            if dados_consulta["data"] is not None:
                existe = True

        if existe:
            self.__tela_consulta.mostra_mensagem("!!!!! HORÁRIO INDISPONÍVEL !!!!!")
        else:
            consulta = Consulta(dados_consulta["codigo"], dados_consulta["cpf"], dados_consulta["data"])
            self.__consultas.append(consulta)

    def lista_consultas(self):
        for consulta in self.__consultas:
            TelaConsulta.mostra_dados_consulta({"codigo": consulta.codigo, "nome_cliente": consulta.__cliente.nome,
                                                "cpf_cliente": consulta.__cliente.cpf, "data": consulta.data})

    def retornar(self):
        self.__controlador_principal.abre_tela()

    def mostra_menu_consulta(self):
        lista_opcoes = {1: self.cadastrar_consulta, 2: self.lista_consultas, 0: self.retornar}
        while True:
            opcao = self.__tela_consulta.lista_opcoes()
            funcao = lista_opcoes[opcao]
            funcao()
