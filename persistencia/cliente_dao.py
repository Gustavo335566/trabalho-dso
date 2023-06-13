from entidade.cliente import Cliente
from persistencia.dao import DAO


class ClienteDAO(DAO):
    def __init__(self):
        super().__init__('clientes.pkl')

    def add(self, chave, cliente: Cliente):
        if isinstance(cliente, Cliente) and cliente is not None:
            super().add(chave, cliente)

    def get(self, key):
        return super().get(key)

    def remove(self, key):
        return super().remove(key)
