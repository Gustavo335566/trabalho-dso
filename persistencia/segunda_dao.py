from persistencia.dao import DAO


class SegundaDAO(DAO):
    def __init__(self):
        super().__init__('segunda.pkl')

    def add(self, chave: str, valor: str):
        if isinstance(valor, str) and valor is not None and isinstance(chave, str) and chave is not None:
            super().add(chave, valor)

    def get(self, key: str):
        return super().get(key)

    def remove(self, key: str):
        return super().remove(key)
