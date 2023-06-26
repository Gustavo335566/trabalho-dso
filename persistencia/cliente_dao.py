from entidade.cliente import Cliente
from persistencia.dao import DAO


class ClienteDAO(DAO):
    def __init__(self):
        super().__init__('clientes.pkl')

    def add(self, key, valor):
        if isinstance(valor, Cliente) and valor is not None:
            super().add(key, valor)

    def get(self, key):
        return super().get(key)

    def remove(self, key):
        return super().remove(key)
