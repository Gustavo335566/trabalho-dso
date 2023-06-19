from entidade.consulta import Consulta
from persistencia.dao import DAO


class TodasConsultasDAO(DAO):
    def __init__(self):
        super().__init__('todas_consultas.pkl')

    def add(self, chave, consulta: Consulta):
        if isinstance(consulta, Consulta) and consulta is not None:
            super().add(chave, consulta)

    def get(self, key: int):
        return super().get(key)

    def remove(self, key: int):
        return super().remove(key)
