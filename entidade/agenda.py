

class Agenda:
    def __int__(self):
            self.__minhas_consultas = [] #um nome melhor para isso ex slots disponiveis

    @property
    def minhas_consultas(self):
        return self.__minhas_consultas

    def add_minhas_consultas(self, consulta: Consulta): #pensar num nome melhor
        if isinstance(consulta, Consulta):
            for i in self.__minhas_consultas():
                if(i == consulta):
                    return "Consulta duplicada" \
            self.__minhas_consultas.append(consulta)
            return f"Consulta adicionada a lista"

    def delete_minhas_consultas(self, consulta: Consulta):
        if isinstance(consulta, Consulta):
            for i in self.__minhas_consultas:
                if(i == consulta):
                    self.__minhas_consultas.remove(consulta)
                    return "Consulta removida"
            return "Consulta nao esta na lista de minhas consultas"
