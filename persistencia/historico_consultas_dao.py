from persistencia.dao import DAO


class HistoricoConsultasDAO(DAO):
    def __init__(self):
        super().__init__('historico_consultas.pkl')

    def add(self, key, valor: str):
        if isinstance(valor, str) and valor is not None:
            super().add(key, valor)

    def get(self, key):
        return super().get(key)

    def remove(self, key):
        return super().remove(key)
