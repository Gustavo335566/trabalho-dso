from persistencia.segunda_dao import SegundaDAO
from persistencia.terca_dao import TercaDAO
from persistencia.quarta_dao import QuartaDAO
from persistencia.quinta_dao import QuintaDAO
from persistencia.sexta_dao import SextaDAO
from entidade.consulta import Consulta

class Agenda:
    __vago = 'vago'
    def __init__(self, tempo_consulta: int):
        self.__segunda_consultas = SegundaDAO()
        self.__terca_consultas = TercaDAO()
        self.__quarta_consulta = QuartaDAO()
        self.__quinta_consulta = QuintaDAO
        self.__sexta_consulta = SextaDAO()
        self.dias_semana(int(tempo_consulta))
        self.__tempo_consulta = int(tempo_consulta)
        self.personalizar_horarios(tempo_consulta)

    '''
    @property
    def segunda_consultas(self):
        return self.__segunda_consultas

    @property
    def terca_consultas(self):
        return self.__terca_consultas

    @property
    def quarta_consultas(self):
        return self.__quarta_consultas

    @property
    def quinta_consultas(self):
        return self.__quinta_consulta

    @property
    def sexta_consultas(self):
        return self.__sexta_consulta
    '''
    def retorna_semana(self):
        linha_horarios = []
        linha_horarios.append(self.__segunda_consultas.get_all())
        linha_horarios.append(self.__terca_consultas.get_all())
        linha_horarios.append(self.__quarta_consultas.get_all())
        linha_horarios.append(self.__quinta_consultas.get_all())
        linha_horarios.append(self.__sexta_consultas.get_all())
        return linha_horarios

    def add_agenda(self, consulta: Consulta):
        if isinstance(consulta, Consulta) and consulta is not None:
            if consulta.data == 'Segunda':
                self.__segunda_consultas.add(consulta.horario, consulta)
            elif consulta.data == 'Terca':
                self.__terca_consultas.add(consulta.horario, consulta)
            elif consulta.data == 'Quarta':
                self.__quarta_consultas.add(consulta.horario, consulta)
            elif consulta.data == 'Quinta':
                self.__quinta_consultas.add(consulta.horario, consulta)
            elif consulta.data == 'Sexta':
                self.__sexta_consultas.add(consulta.horario, consulta)

    def remove_agenda(self, dia, hora):
        if dia == 'Segunda':
            self.__segunda_consultas.add(hora, Agenda.__vago)
            return True
        elif dia == 'Terca':
            self.__terca_consultas.add(hora, Agenda.__vago)
            return True
        elif dia == 'Quarta':
            self.__quarta_consultas.add(hora, Agenda.__vago)
            return True
        elif dia == 'Quinta':
            self.__quinta_consultas.add(hora, Agenda.__vago)
            return True
        elif dia == 'Sexta':
            self.__sexta_consultas.add(hora, Agenda.__vago)
            return True
        return False

    @property
    def tempo_consulta(self):
        return self.__tempo_consulta

    @tempo_consulta.setter
    def tempo_consulta(self, tempo_consulta: int):
        self.__tempo_consulta = int(tempo_consulta)

    def personalizar_horarios(self, tempo_consulta):
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
                    hora = f"{str(i)}:00"
                    self.__segunda_consultas.add(hora, self.__vago)
                    self.__terca_consultas.add(hora, self.__vago)
                    self.__quarta_consulta.add(hora, self.__vago)
                    self.__quinta_consulta.add(hora, self.__vago)
                    self.__sexta_consulta.add(hora, self.__vago)
                else:
                    hora = f"{str(i)}:{str(cont)}"
                    self.__segunda_consultas.add(hora, self.__vago)
                    self.__terca_consultas.add(hora, self.__vago)
                    self.__quarta_consulta.add(hora, self.__vago)
                    self.__quinta_consulta.add(hora, self.__vago)
                    self.__sexta_consulta.add(hora, self.__vago)
                if int(tempos) == 1 and tempo_consulta != 60:
                    cont += tempo_consulta
                    if cont >= 60:
                        cont = cont - 60
                        break
                    hora = f"{str(i)}:{str(cont)}"
                    self.__segunda_consultas.add(hora, self.__vago)
                    self.__terca_consultas.add(hora, self.__vago)
                    self.__quarta_consulta.add(hora, self.__vago)
                    self.__quinta_consulta.add(hora, self.__vago)
                    self.__sexta_consulta.add(hora, self.__vago)
                cont += tempo_consulta
