from entidade.consulta import Consulta
from limite.tela_agenda import TelaAgenda


class ControladorAgenda:
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__tela_agenda = TelaAgenda()

    def inclui_consulta(self, usuario):
        if self.__controlador_principal.controlador_cliente.numero_clientes() > 0:
            consulta = self.__controlador_principal.controlador_consulta.cadastrar_consulta(usuario)
            self.__controlador_principal.controlador_consulta.add_consulta(consulta)
            if isinstance(consulta, Consulta):
                for data, horarios in usuario.agenda.minhas_consultas.items():
                    if data == consulta.data:
                        for k, v in horarios.items():
                            if v == "vago" and k == consulta.horario:
                                horarios[k] = consulta
                self.__tela_agenda.mostra_mensagem(f"{consulta} cadastrada com sucesso")
        else:
            self.__tela_agenda.mostra_mensagem("Cliente nao cadastrado")
        input()

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

    def mostrar_horarios(self, usuario):
        self.__tela_agenda.mostra_mensagem("-------Minhas consultas------")
        for data, horarios in usuario.agenda.minhas_consultas.items():
            self.__tela_agenda.mostra_mensagem(data)
            for hora, consulta in horarios.items():
                self.__tela_agenda.imprimir(hora, consulta)
            self.__tela_agenda.no_lado()
        self.__tela_agenda.stop()

    def menu_agenda(self, usuario):
        switcher = {1: self.inclui_consulta,
                    2: self.exclui_consulta,
                    3: self.mostrar_horarios,
                    4: self.procura_consulta}
        while True:
            opcao = self.__tela_agenda.menu_agenda()
            if opcao == 0:
                break
            funcao_escolhida = switcher[opcao]
            funcao_escolhida(usuario)

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
