from persistencia.dao import DAO


class AgendasDAO(DAO):
    def __init__(self):
        super().__init__('agendas.pkl')

    def add(self, cpf_usuario, agenda):
        if agenda is not None:
            super().add(cpf_usuario, agenda)

    def get(self, key):
        return super().get(key)

    def remove(self, key):
        return super().remove(key)
