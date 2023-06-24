from entidade.consulta import Consulta
from limite.tela_agenda import TelaAgenda


class ControladorAgenda:
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__tela_agenda = TelaAgenda(self)

    def inclui_consulta(self):
        usuario = self.__controlador_principal.controlador_usuario.usuario_logado
        if self.__controlador_principal.controlador_cliente.numero_clientes() > 0:
            consulta = self.__controlador_principal.controlador_consulta.cadastrar_consulta()
            if isinstance(consulta, Consulta):
                usuario.agenda.add_agenda(consulta)
                self.__tela_agenda.mostra_mensagem(f"{consulta} cadastrada com sucesso")
                self.__tela_agenda.open(self.mostrar_horarios())
        else:
            self.__tela_agenda.mostra_mensagem("Cliente nao cadastrado")

    def exclui_consulta(self, usuario):
        if self.se_tem_consultas(usuario):
            #consulta = self.__controlador_principal.controlador_consulta.exclui_consulta()
            #dia e a hora
            controle = usuario.agenda.remove_agenda(dia, hora)
            if controle:
                self.__tela_agenda.mostra_mensagem('exclusão alterada com sucesso')
            else:
                self.__tela_agenda.mostra_mensagem('exclusão falhou')

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
        usuario = self.__controlador_principal.controlador_usuario.usuario_logado
        linha_horarios = usuario.agenda.retorna_semana()
        return linha_horarios

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
        self.__tela_agenda.open(self.mostrar_horarios())

    @property
    def tela_agenda(self):
        return self.__tela_agenda