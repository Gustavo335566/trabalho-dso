from entidade.consulta import Consulta
from persistencia.dao import DAO


class TodasConsultasDAO(DAO):
    def __init__(self):
        super().__init__('todas_consultas.pkl')

    def add(self, key, valor: Consulta):
        if isinstance(valor, Consulta) and valor is not None:
            super().add(key, valor)

    def get(self, key: int):
        return super().get(key)

    def remove(self, key: int):
        return super().remove(key)
