from entidade.agenda import Agenda
from limite.tela_agenda import Tela_Agenda

class Controlador_Agenda(Agenda, Tela_Agenda):
    def __init__(self, controlador_principal, Controlador_Principal):
        self.__controlador_principal = controlador_principal
        self.__tela_agenda = Tela_Agenda()

