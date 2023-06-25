from entidade.consulta import Consulta
from limite.tela_agenda import TelaAgenda
from persistencia.agendas_dao import AgendasDAO
from entidade.agenda import Agenda


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
            consulta = self.__controlador_principal.controlador_consulta.cadastrar_consulta()
            self.__controlador_principal.controlador_consulta.add_consulta(consulta)
            if isinstance(consulta, Consulta):
                for data, horarios in self.__agenda_usuario_logado.minhas_consultas.items():
                    if data == consulta.data:
                        for k, v in horarios.items():
                            if v == "vago" and k == consulta.horario:
                                horarios[k] = consulta
                self.atualiza_agenda_usuario(self.__agenda_usuario_logado)
                self.__tela_agenda.mostra_mensagem(f"{consulta} cadastrada com sucesso")
                self.__tela_agenda.open()
        else:
            self.__tela_agenda.mostra_mensagem("Cliente nao cadastrado")

    def exclui_consulta(self, usuario):
        if self.se_tem_consultas(usuario):
            consulta = self.__controlador_principal.controlador_consulta.exclui_consulta()
            if consulta is not str:
                for data, horarios in usuario.agenda.minhas_consultas.items():
                    for hora, v in horarios.items():
                        if consulta == v:
                            horarios[hora] = "vago"
                            self.__tela_agenda.mostra_mensagem("Consulta excluida")
            else:
                self.__tela_agenda.mostra_mensagem(consulta)
        else:
            self.__tela_agenda.mostra_mensagem('não há consultas para excluir')
        input()

    def pega_consulta_por_cpf(self):
        cliente = self.__controlador_principal.controlador_cliente.pega_cliente_por_cpf()
        codigo = self.__controlador_principal.controlador_consulta.pega_codigo_por_cliente(cliente)
        return codigo

    def procura_consulta(self, usuario):
        if self.__controlador_principal.controlador_cliente.numero_clientes() > 0:
            cont = True
            cliente = self.__controlador_principal.controlador_cliente.pega_cliente_por_cpf()
            for data, horarios in usuario.agenda.minhas_consultas.items():
                for hora, consulta in horarios.items():
                    if not isinstance(consulta, str):
                        if consulta.cliente == cliente:
                            cont = False
                            self.__tela_agenda.imprimir_consulta(consulta)
            if cont:
                self.__tela_agenda.mostra_mensagem('não consultas com esse cpf')
            input()
        elif self.se_tem_consultas(usuario) == None:
            self.__tela_agenda.mostra_mensagem('não há consultas cadastradas')
        else:
            self.__tela_agenda.mostra_mensagem("não há clientes cadastrados")
        input()

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

    def se_tem_consultas(self, usuario):
        cont = False
        for k, v in usuario.agenda.minhas_consultas.items():
            for hora, disponibilidade in v.items():
                if disponibilidade != 'vago':
                    cont = True
        if cont:
            return cont
        else:
            return None

    def abrir_tela(self):
        self.__tela_agenda.open()

    @property
    def tela_agenda(self):
        return self.__tela_agenda

    def atualiza_agenda_usuario(self, minhas_consultas):
        usuario = self.__controlador_principal.controlador_usuario.usuario_logado
        self.__agenda_dao.remove(usuario.cpf)
        print(self.__agenda_dao.get(usuario.cpf))
        self.__agenda_dao.add(usuario.cpf, minhas_consultas)

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
