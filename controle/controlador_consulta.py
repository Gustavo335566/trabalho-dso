from entidade.consulta import Consulta
from controle.controlador_cliente import ControladorClientes
from limite.tela_consulta import TelaConsulta
from persistencia.todas_consultas_dao import TodasConsultasDAO
from persistencia.historico_consultas_dao import HistoricoConsultasDAO

class ControladorConsulta:
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__historico_consultas = HistoricoConsultasDAO()
        self.__todas_consultas = TodasConsultasDAO()
        self.__tela_consulta = TelaConsulta(self)
        #ADICIONAR CONSULTA AO HISTORICO

    @property
    def todas_consultas(self):
        return self.__todas_consultas.get_all()

    def add_consulta(self, consulta):
        if isinstance(consulta, Consulta):
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
    def cadastrar_consulta(self):
        existe_cliente = False
        existe = True
        usuario = self.__controlador_principal.controlador_usuario.usuario_logado
        agenda = self.__controlador_principal.controlador_agenda.agenda_usuario_logado
        dados_consulta = self.__controlador_principal.controlador_agenda.tela_agenda.open_cadastro_consulta()
        cliente = self.__controlador_principal.controlador_cliente.pega_cliente_por_cpf(dados_consulta["cpf"])
        for cl in self.__controlador_principal.controlador_cliente.cliente_dao.get_all():
            if cliente == cl:
                existe_cliente = True
        if existe_cliente:
            for data, horarios in agenda.minhas_consultas.items():
                for hora, valor in horarios.items():
                    if data == dados_consulta["data"]:
                        if hora == dados_consulta["hora"] and valor == "vago":
                            existe = False
            if existe:
                self.__tela_consulta.mostra_mensagem("!!!!! HORÁRIO INDISPONÍVEL !!!!!")
            else:
                consultas_marcadas = []
                for horarios in agenda.minhas_consultas.values():
                    for consulta in horarios.values():
                        if consulta != "vago":
                            consultas_marcadas.append(consulta)
                codigo = 1000 + len(consultas_marcadas)
                consulta = Consulta(cliente, dados_consulta["data"], dados_consulta["hora"], codigo)
                self.__historico_consultas.add(consulta.codigo, f"{dados_consulta} adicionado")
                self.__todas_consultas.add(consulta.codigo, consulta)
                return consulta

    def exclui_consulta(self, consulta):
        if consulta is not str:
            self.__historico_consultas.add(consulta.codigo, f"{consulta} removido com sucesso")
            self.__tela_consulta.mostra_mensagem(f"{consulta} removido com sucesso")
            self.__todas_consultas.remove(consulta.codigo)

    @property
    def historico_consultas(self):
        return self.__historico_consultas.get_all()
