from entidade.usuario import Usuario
from persistencia.dao import DAO


class UsuarioDAO(DAO):
    def __init__(self):
        super().__init__('usuarios.pkl')

    def add(self, chave, usuario: Usuario):
        if isinstance(usuario, Usuario) and usuario is not None:
            super().add(chave, usuario)

    def get(self, key: str):
        return super().get(key)

    def remove(self, key: str):
        return super().remove(key)
