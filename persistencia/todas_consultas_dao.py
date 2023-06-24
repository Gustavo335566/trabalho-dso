from entidade.consulta import Consulta
from persistencia.dao import DAO


class TodasConsultasDAO(DAO):
    def __init__(self):
        super().__init__('todas_consultas.pkl')

    def add(self, chave: str, consulta: Consulta):
        if isinstance(consulta, Consulta) and consulta is not None and isinstance(chave, str) and chave is not None:
            super().add(chave, consulta)

    def get(self, key: str):
        return super().get(key)

    def remove(self, key: str):
        return super().remove(key)
