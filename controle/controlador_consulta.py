from entidade.consulta import Consulta
from persistencia.todas_consultas_dao import TodasConsultasDAO
from persistencia.historico_consultas_dao import HistoricoConsultasDAO


class ControladorConsulta:
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__historico_consultas = HistoricoConsultasDAO()
        self.__todas_consultas = TodasConsultasDAO()


    def cria_consulta(self, dados_consulta):
        consulta = Consulta(dados_consulta["cliente"], dados_consulta["data"],
                            dados_consulta["hora"], dados_consulta["codigo"])
        return consulta


    @property
    def todas_consultas(self):
        return self.__todas_consultas.get_all()

    def add_consulta(self, consulta):
        if isinstance(consulta, Consulta):
            self.__todas_consultas.add(consulta.codigo, consulta)

    def verifica_se_tem_consulta(self, cliente):
        for consulta in self.__todas_consultas.get_all():
            if consulta.cliente.cpf == cliente.cpf:
                return True
        return False

    @property
    def historico_consultas(self):
        return self.__historico_consultas
