from abc import ABC, abstractmethod


class Pessoa(ABC):
    @abstractmethod
    def __init__(self, nome: str, cpf: int, telefone: int, sexo: str):
        self.__nome = nome
        self.__cpf = cpf
        self.__telefone = telefone
        self.__sexo = sexo

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, Pessoa) or nome is not None:
            self.__nome = nome

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf: int):
        if isinstance(cpf, Pessoa) and cpf is not None:
            self.__cpf = cpf

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone: int):
        if isinstance(telefone, Pessoa) and telefone is not None:
            self.__telefone = telefone

    @property
    def sexo(self):
        return self.__sexo

    @sexo.setter
    def sexo(self, sexo: str):
        if isinstance(sexo, Pessoa) and sexo is not None:
            self.__sexo = sexo
