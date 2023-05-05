from entidade.agenda import Agenda
from limite.tela_agenda import Tela_Agenda

class Controlador_Agenda(Agenda, Tela_Agenda):
    def __init__(self, controlador_principal, Controlador_Principal):
        self.__controlador_principal = controlador_principal
        self.__tela_agenda = Tela_Agenda()

    def ver_agenda(self):
        mostra = self.minhas_consultas
        Tela_Agenda().imprimir(mostra)

    def inclui_consulta(self, consulta: Consulta):
        if isinstance(consulta, Consulta):
            for i in self.minhas_consultas:
                if(consulta == i):
                    return "Consulta duplicada"
            self.minhas_consultas.append(consulta)
            return "Consulta incluida"

    def exclui_consulta(self, consulta: Consulta):
        if isinstance(consulta, Consulta):
            for i in self.minhas_consultas:
                if(consulta == i):
                    self.minhas_consultas.remove(consulta)
                    return "Consulta excluida"
            return "Consulta inexistente"

    def Altera_consulta(self, consulta: Consulta):
        if isinstance(consulta, Consulta):
            for i in self.minhas_consultas:
                if(consulta == i):
                    return self.minhas_consultas[i]
            return "Consulta inexistente"
