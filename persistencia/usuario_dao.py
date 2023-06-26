from entidade.usuario import Usuario
from persistencia.dao import DAO


class UsuarioDAO(DAO):
    def __init__(self):
        super().__init__('usuarios.pkl')

    def add(self, key, valor):
        if isinstance(valor, Usuario) and valor is not None:
            super().add(key, valor)

    def get(self, key: str):
        return super().get(key)

    def remove(self, key: str):
        return super().remove(key)
