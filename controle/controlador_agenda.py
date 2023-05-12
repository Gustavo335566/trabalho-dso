from entidade.agenda import Agenda
from limite.tela_agenda import Tela_Agenda
from controle.controlador_consulta import ControladorConsulta
from controle.controlador_cliente import ControladorClientes
class Controlador_Agenda(Agenda, Tela_Agenda, ControladorPrincipal, ControladorConsulta, ControladorClientes):
    def __init__(self, controlador_principal: ControladorPrincipal):
        self.__controlador_principal = controlador_principal
        self.__tela_agenda = Tela_Agenda()
        self.__controlador_consulta = ControladorConsulta
        self.__controlador_cliente = ControladorClientes

    def inclui_consulta(self, consulta: Consulta):
        if isinstance(consulta, Consulta):
            for i in self.minhas_consultas:
                if(i == consulta.datas_consulta):
                    for k, v in i.items():
                        if(v == "vago" and k == consulta.horario):
                            v[k] = consulta
                        self.minhas_consultas.append(consulta)
            return "Consulta incluida"

    def exclui_consulta(self):
        if isinstance(consulta, Consulta):
            for i in self.minhas_consultas:
                for k,v in i.items():
                    if(codigo == v.codigo):
                        i[k] = "vago"
                        return "Consulta excluida"
            return "Consulta inexistente"

    def Altera_consulta(self, consulta: Consulta):
        if isinstance(consulta, Consulta):
            for i in self.minhas_consultas:
                if(consulta == i):
                    return self.minhas_consultas[i]
            return "Consulta inexistente"

    def finalizar(self):
        exit(0)

    def procura_consulta(self):
        codigo = self.__controlador_cliente.pega_cliente_por_cpf()
        for i in self.minhas_consultas:
            for k,v in i.items():
                if(v.codigo == codigo):
                    self.__tela_agenda.imprimir_consulta(k,v)

    def menu_agenda(self):
        switcher = {0: self.finalizar(), 1: self.exclui_consulta(), 2: self.__tela_agenda.imprimir(self.minhas_consultas),
                    3: self.procurar_consulta}
        while True:
            opcao = Tela_Agenda().Tela_Menu()
            funcao_escolhida = switcher[opcao]
            funcao_escolhida()
            """lista = [0, 1, 2, 3, 4, 5]
            while(opcao in not lista):
                return "opcao invalida"
            if(opcao == 1):
                mensagem = inclui_consulta(ControladorConsulta.mostra_menu_consulta())
                Tela_Agenda().inclui(mensagem)
            elif(opcao == 2):
                cliente = ControladorCliente.pega_cliente_por_cpf(Tela_Agenda.pega_cpf_cliente())
                if(cliente == "CPF NAO CADASTRADO"):
                    mensagem = cliente
                    Tela_Agenda.exclui(mensagem)
                mensagem = ControladorConsulta.pega_codigo_por_cliente(cliente)
                if(mensagem == """"Tenho que colocar a mensagem or mensagem == """"Tenho que colocar a mensagem):
                    Tela_Agenda.exclui(mensagem)
                else:
                    codigo = mensagem
                    Tela_Agenda.exclui(exclui_consulta(codigo))
            elif(opcao == 3):
                Tela_Agenda.imprimir(self.minhas_consultas)
            elif(opcao == 4):
                Tela_Agenda.imprimir_consulta(ControladorConsulta.pega_consulta_por_codigo(ControladorConsulta.pega_codigo_por_cliente(Tela_Agenda.pega_cpf_cliente())))
            elif(opcao == 0):
                break"""
