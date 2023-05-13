

class Agenda:
    def __init__(self, tempo_consulta: int):
        self.__minhas_consultas = []
        self.dias_semana(tempo_consulta) #um nome melhor para isso ex slots disponiveis
        self.__tempo_consulta = tempo_consulta

    @property
    def minhas_consultas(self):
        return self.__minhas_consultas

    @property
    def tempo_consulta(self):
        return self.__tempo_consulta

    @tempo_consulta.setter
    def tempo_consulta(self, tempo_consulta: int):
        self.__tempo_consulta = tempo_consulta

    def personalizar_horarios(self, tempo_consulta):
        horarios = {}
        divisao = 60//int(tempo_consulta)
        for i in range(8, 18):
            cont = 0
            for j in range(divisao):
                horarios[str(i)+":"+ str(cont)] = "vago"
                cont += tempo_consulta
        return horarios

    def dias_semana(self, tempo_consulta):
        segunda = self.personalizar_horarios(tempo_consulta)
        self.__minhas_consultas.append(segunda)
        terca = segunda.copy()
        self.__minhas_consultas.append(terca)
        quarta = terca.copy()
        self.__minhas_consultas.append(quarta)
        quinta = quarta.copy()
        self.__minhas_consultas.append(quinta)
        sexta = quinta.copy()
        self.__minhas_consultas.append(sexta)
