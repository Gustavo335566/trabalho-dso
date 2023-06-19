from persistencia.dao import DAO


class HistoricoConsultasDAO(DAO):
    def __init__(self):
        super().__init__('historico_consultas.pkl')

    def add(self, chave, observação: str):
        if isinstance(observação, str) and observação is not None:
            super().add(chave, observação)

    def get(self, key):
        return super().get(key)

    def remove(self, key):
        return super().remove(key)
