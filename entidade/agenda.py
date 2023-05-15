

class Agenda:
    def __init__(self, tempo_consulta: int):
        self.__minhas_consultas = {}
        self.dias_semana(tempo_consulta)
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
        cont = 0
        divisao = 60 / tempo_consulta
        tempos = round(divisao)
        for i in range(8, 18):
            if cont >= 60:
                cont = cont - 60
            for j in range(int(tempos)):
                if cont >= 60:
                    cont = cont - 60
                    break
                if cont == 0:
                    horarios[f"{str(i)}:00"] = "vago"
                else:
                    horarios[f"{str(i)}:{str(cont)}"] = "vago"
                if int(tempos) == 1 and tempo_consulta != 60:
                    cont += tempo_consulta
                    if cont >= 60:
                        cont = cont - 60
                        break
                    horarios[f"{str(i)}:{str(cont)}"] = "vago"
                cont += tempo_consulta
        return horarios

    def dias_semana(self, tempo_consulta):
        self.__minhas_consultas["Segunda"] = self.personalizar_horarios(tempo_consulta)
        self.__minhas_consultas["Terça"] = self.personalizar_horarios(tempo_consulta)
        self.__minhas_consultas["Quarta"] = self.personalizar_horarios(tempo_consulta)
        self.__minhas_consultas["Quinta"] = self.personalizar_horarios(tempo_consulta)
        self.__minhas_consultas["Sexta"] = self.personalizar_horarios(tempo_consulta)
