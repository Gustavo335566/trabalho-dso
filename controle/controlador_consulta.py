from entidade.consulta import Consulta
from controle.controlador_cliente import ControladorClientes
from limite.tela_consulta import TelaConsulta
from persistencia.todas_consultas_dao import TodasConsultasDAO
from persistencia.historico_consultas_dao import HistoricoConsultasDAO

class ControladorConsulta:
    __CONTADOR_CODIGO = 1000
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__historico_consultas = HistoricoConsultasDAO()
        self.__todas_consultas = TodasConsultasDAO()
        self.__tela_consulta = TelaConsulta(self)
        #ADICIONAR CONSULTA AO HISTORICO

    @property
    def contador_codigo(self):
        return self.__CONTADOR_CODIGO

    @property
    def todas_consultas(self):
        return self.__todas_consultas.get_all()

    def add_consulta(self, consulta):
        self.__todas_consultas.add(consulta.codigo, consulta)

    def verifica_se_tem_consulta(self, cliente):
        for consulta in self.__todas_consultas.get_all():
            if consulta.cliente == cliente:
                return True
        return False

    def pega_codigo_por_cliente(self, cliente):
        for consulta in self.__todas_consultas.get_all():
            if consulta.cliente == cliente:
                self.__tela_consulta.mostra_mensagem(consulta)
        codigo = self.__tela_consulta.seleciona_consulta()
        consulta_escolhida = self.pega_consulta_por_codigo(codigo)
        if len(self.todas_consultas) > 0:
            for consulta in self.__todas_consultas.get_all():
                if consulta.cliente == cliente and consulta == consulta_escolhida:
                    return consulta.codigo
            return "CLIENTE NAO POSSUI CONSULTA"
        return "sem consultas cadastradas"

    def pega_consulta_por_codigo(self, codigo):
        for consulta in self.__historico_consultas.get_all():
            if consulta.codigo == codigo:
                return consulta
        return "CONSULTA NAO EXISTENTE"

    def cadastrar_consulta(self, usuario):
        existe_cliente = False
        existe = True
        self.__CONTADOR_CODIGO += 1
        codigo = self.__CONTADOR_CODIGO
        dados_consulta = self.__tela_consulta.pega_dados_consulta(self.__controlador_principal.controlador_cliente.pega_cliente_por_cpf(), usuario)
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
                self.__historico_consultas.add(consulta.codigo, f"{dados_consulta} adicionado")
                self.__todas_consultas.add(consulta.codigo, consulta)
                return consulta

    def lista_consultas(self):
        for consulta in self.__historico_consultas.get_all():
            self.__tela_consulta.mostra_dados_consulta({"codigo": consulta.codigo,
                                                        "cliente": consulta.cliente,
                                                        "data": consulta.data})

    def exclui_consulta(self):
        self.lista_consultas()
        codigo = self.__tela_consulta.seleciona_consulta()
        consulta = self.pega_consulta_por_codigo(codigo)
        if consulta is not str:
            self.__historico_consultas.add(consulta.codigo, f"{consulta} removido com sucesso")
            self.__tela_consulta.mostra_mensagem(f"{consulta} removido com sucesso")
            self.__todas_consultas.remove(consulta.codigo)
            return consulta
        else:
            return "!!!! CONSULTA NÃO CADASTRADA !!!!"

    @property
    def historico_consultas(self):
        return self.__historico_consultas.get_all()
