from abc import ABC, abstractmethod


class Pessoa(ABC):
    @abstractmethod
    def __init__(self, nome: str, cpf: str, telefone: str, sexo: str):
        if isinstance(nome, str):
            self.__nome = nome
        else:
            self.__nome = None
        if len(cpf) == 11 and isinstance(cpf, str):
            self.__cpf = cpf
        else:
            self.__cpf = None
        if len(telefone) >= 11 or len(telefone) < 12 and isinstance(telefone, str):
            self.__telefone = telefone
        else:
            self.__telefone = None
        if sexo.upper() in "MF" and isinstance(sexo, str):
            self.__sexo = sexo
        else:
            self.__sexo = None

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str) and nome is not None:
            self.__nome = nome

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf: str):
        if isinstance(cpf, str) and len(cpf) == 11:
            self.__cpf = cpf

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone: str):
        if isinstance(telefone, str) and len(telefone) >= 11 or len(telefone) <= 12:
            self.__telefone = telefone

    @property
    def sexo(self):
        return self.__sexo

    @sexo.setter
    def sexo(self, sexo: str):
        if isinstance(sexo, str) and sexo.upper() in "MF":
            self.__sexo = sexo
