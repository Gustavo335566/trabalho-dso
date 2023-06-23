from persistencia.dao import DAO


class MinhasConsultasDAO(DAO):
    def __init__(self):
        super().__init__('minhas_consultas.pkl')

    def add(self, cpf_usuario, consultas: str):
        if isinstance(consultas, str) and consultas is not None:
            super().add(cpf_usuario, consultas)

    def get(self, key):
        return super().get(key)

    def remove(self, key):
        return super().remove(key)
