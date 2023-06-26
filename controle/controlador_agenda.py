from limite.tela_agenda import TelaAgenda
from persistencia.agendas_dao import AgendasDAO
from entidade.agenda import Agenda
from excecoes.horario_ja_reservado_exception import HorarioJaReservado


class ControladorAgenda:
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__tela_agenda = TelaAgenda(self)
        self.__agenda_dao = AgendasDAO()
        self.__agenda_usuario_logado = None

    @property
    def agenda_dao(self):
        return self.__agenda_dao

    def inclui_consulta(self):
        usuario = self.__controlador_principal.controlador_usuario.usuario_logado
        if self.__controlador_principal.controlador_cliente.numero_clientes() > 0:
            self.__agenda_usuario_logado.codigo_atual += 1
            existe_cliente = False
            horario_disponivel = False
            dados_consulta = self.__tela_agenda.open_cadastro_consulta()
            cliente = self.__controlador_principal.controlador_cliente.pega_cliente_por_cpf(dados_consulta["cpf"])
            for cl in self.__controlador_principal.controlador_cliente.cliente_dao.get_all():
                if cliente == cl:
                    existe_cliente = True
            if existe_cliente:
                for data, horarios in self.__agenda_usuario_logado.minhas_consultas.items():
                    for hora, valor in horarios.items():
                        if data == dados_consulta["data"]:
                            if hora == dados_consulta["hora"] and valor == "vago":
                                horario_disponivel = True
                try:
                    if not horario_disponivel:
                        raise HorarioJaReservado("HORARIO INDISPONIVEL")
                    else:
                        consulta = self.__controlador_principal.controlador_consulta.cria_consulta({"cliente": cliente,
                                                                                                    "data":
                                                                                                        dados_consulta[
                                                                                                            "data"],
                                                                                                    "hora":
                                                                                                        dados_consulta[
                                                                                                            "hora"],
                                                                                                    "codigo": self.__agenda_usuario_logado.codigo_atual})
                        self.__agenda_usuario_logado.minhas_consultas[dados_consulta["data"]][
                            dados_consulta["hora"]] = consulta
                        self.atualiza_agenda_usuario(self.__agenda_usuario_logado)
                        self.__tela_agenda.mostra_mensagem("Atencao", f"{consulta} cadastrada com sucesso")
                        self.__tela_agenda.open()
                except HorarioJaReservado as hjr:
                    self.__tela_agenda.mostra_mensagem("Atencao", hjr)
            else:
                self.__tela_agenda.mostra_mensagem("Atencao", "Cliente nao cadastrado")

    def exclui_consulta(self, codigo_consulta):
        consulta = self.pega_consulta_por_codigo(codigo_consulta)
        if consulta is not str:
            for data, horarios in self.__agenda_usuario_logado.minhas_consultas.items():
                for hora, v in horarios.items():
                    if consulta == v:
                        horarios[hora] = "vago"
                        self.__controlador_principal.controlador_usuario__historico_consultas.add(consulta.codigo, f"{consulta} removido com sucesso")
                        self.__controlador_principal.controlador_consulta.__todas_consultas.remove(consulta.codigo)
                        self.__tela_agenda.mostra_mensagem("Atencao", "CONSULTA EXCLUIDA")
                        self.atualiza_agenda_usuario(self.__agenda_usuario_logado)

    def pega_consulta_por_codigo(self, codigo):
        for horarios in self.__agenda_usuario_logado.minhas_consultas.values():
            for consulta in horarios.values():
                if not isinstance(consulta, str):
                    if consulta.codigo == int(codigo):
                        return consulta

    def buscar_consulta(self, codigo_consulta: int):
        consulta = self.pega_consulta_por_codigo(codigo_consulta)
        if not consulta:
            self.__tela_agenda.mostra_mensagem("Atencao", "CONSULTA NAO CADASTRADA")
        else:
            self.__tela_agenda.open_dados_consulta({"nome": consulta.cliente.nome, "cpf": consulta.cliente.cpf,
                                                    "data": consulta.data, "hora": consulta.horario,
                                                    "codigo": consulta.codigo})

    def mostrar_horarios(self):
        horarios_do_usuario = self.__agenda_usuario_logado.minhas_consultas
        lista_horarios = [[horario] for horario in horarios_do_usuario["Segunda"]]
        for data, horarios in horarios_do_usuario.items():
            for i, hora in enumerate(horarios.keys()):
                consulta = horarios[hora]
                if isinstance(consulta, str):
                    lista_horarios[i].append(consulta)
                else:
                    lista_horarios[i].append(consulta.codigo)
        return lista_horarios

    def abrir_tela(self):
        self.__tela_agenda.open()

    @property
    def tela_agenda(self):
        return self.__tela_agenda

    def atualiza_agenda_usuario(self, nova_agenda):
        usuario = self.__controlador_principal.controlador_usuario.usuario_logado
        self.__agenda_dao.add(usuario.cpf, nova_agenda)

    def criar_agenda_usuario(self, cpf_usuario, tempo_consulta: int, ):
        agenda = Agenda(tempo_consulta)
        self.__agenda_dao.add(cpf_usuario, agenda)
        return agenda

    @property
    def agenda_usuario_logado(self):
        return self.__agenda_usuario_logado

    @agenda_usuario_logado.setter
    def agenda_usuario_logado(self, nova_agenda):
        self.__agenda_usuario_logado = nova_agenda

    def consulta_feita(self, dados_consulta):
        usuario = self.__controlador_principal.controlador_usuario.usuario_logado
        cliente = self.__controlador_principal.controlador_cliente.pega_cliente_por_cpf(dados_consulta["cpf"])
        if not isinstance(cliente, str):
            for data, horarios in self.agenda_usuario_logado.minhas_consultas.items():
                for hora, consulta in horarios.items():
                    if consulta != "vago":
                        if consulta.cliente.cpf == cliente.cpf:
                            if int(dados_consulta["codigo"]) == int(consulta.codigo):
                                usuario.relatorio.append(consulta)
                                horarios[hora] = "vago"
                                adicione_historico = self.__controlador_principal.controlador_cliente\
                                    .adicionar_no_historico(consulta, usuario)
                                self.__controlador_principal.controlador_consulta.\
                                    historico_consultas.add(dados_consulta["codigo"], adicione_historico)
                                self.atualiza_agenda_usuario(self.__agenda_usuario_logado)
                                return 0
