from persistencia.dao import DAO


class HistoricoConsultasDAO(DAO):
    def __init__(self):
        super().__init__('historico_consultas.pkl')

    def add(self, chave: str, observacao: str):
        if isinstance(observacao, str) and observacao is not None and isinstance(chave, str) and chave is not None:
            super().add(chave, observacao)

    def get(self, key):
        return super().get(key)

    def remove(self, key):
        return super().remove(key)
