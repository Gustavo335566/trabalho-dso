from abc import ABC, abstractmethod


class Pessoa(ABC):
    @abstractmethod
    def __init__(self, nome: str, cpf: str, telefone: str, sexo: str):
        self.__nome = nome
        self.__cpf = cpf
        self.__telefone = telefone
        self.__sexo = sexo

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        nome_comprimido = nome.replace(" ", "")
        if isinstance(nome, str) and nome_comprimido.isalpha():
            self.__nome = nome.title()

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf: str):
        if isinstance(cpf, str) and len(cpf) == 11 and cpf.isdigit():
            self.__cpf = cpf

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone: str):
        if isinstance(telefone, str) and len(telefone) >= 11:
            self.__telefone = telefone

    @property
    def sexo(self):
        return self.__sexo

    @sexo.setter
    def sexo(self, sexo: str):
        if isinstance(sexo, str) and (sexo.upper() in "M" or sexo.upper() in "F"):
            self.__sexo = sexo.upper()
