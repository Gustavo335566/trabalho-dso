from persistencia.dao import DAO


class AgendasDAO(DAO):
    def __init__(self):
        super().__init__('agendas.pkl')

    def add(self, key, valor):
        if key is not None:
            super().add(key, valor)

    def get(self, key):
        return super().get(key)

    def remove(self, key):
        return super().remove(key)
