from entidade.usuario import Usuario
from limite.tela_usuario import TelaUsuario
from persistencia.usuario_dao import UsuarioDAO


class ControladorUsuario:
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__tela_usuario = TelaUsuario(self)
        self.__usuario_dao = UsuarioDAO()
        self.__usuario_logado = None

    @property
    def usuario_dao(self):
        return self.__usuario_dao

    def cadastro_usuario(self, dados_usuario):
        existe = False
        for usuario in self.__usuario_dao.get_all():
            if usuario.nome_usuario == dados_usuario["nome_usuario"]:
                self.__tela_usuario.mostra_mensagem("Atencao", "NOME DE USUARIO INDISPONIVEL")
                existe = True
            elif usuario.cpf == dados_usuario["cpf"]:
                self.__tela_usuario.mostra_mensagem("Atencao", "CPF JA CADASTRADO")
                existe = True
        if not existe:
            usuario = Usuario(dados_usuario["nome"], dados_usuario["cpf"], dados_usuario["telefone"],
                              dados_usuario["sexo"], dados_usuario["nome_usuario"], dados_usuario["senha_usuario"],
                              dados_usuario["tempo_consulta"], dados_usuario["preco_consulta"], "Funcionario")
            agenda = self.__controlador_principal.controlador_agenda.criar_agenda_usuario(usuario.cpf, usuario.tempo_consulta)
            self.__usuario_dao.add(usuario.cpf, usuario)
            mensagem = "cadastro realizado com sucesso"
            self.__tela_usuario.mostra_mensagem("Aviso", mensagem)

    def alterar_usuario(self, dados_usuario):
        self.__usuario_logado.nome = dados_usuario["nome"]
        self.__usuario_logado.sexo = dados_usuario["sexo"]
        self.__usuario_logado.nome_usuario = dados_usuario["nome_usuario"]
        self.__usuario_logado.senha_usuario = dados_usuario["senha_usuario"]
        self.__usuario_logado.telefone = dados_usuario["telefone"]
        self.__usuario_logado.preco_consulta = dados_usuario["preco_consulta"]
        self.usuario_dao.add(self.usuario_logado.cpf, self.usuario_logado)

    def historico_sistema(self):
        historico = self.__controlador_principal.controlador_consulta.historico_consultas
        for i in historico:
            self.__tela_usuario.mostra_mensagem(i)
        input()

    def calculo_financeiro(self):
        calculo = len(self.__usuario_logado.relatorio) * self.__usuario_logado.preco_consulta
        self.__tela_usuario.mostra_mensagem("Relatorio Financeiro", f"Total ganho: R${calculo:.2f}")

    def pega_dados_usuario(self):
        usuario = self.__usuario_logado
        dados_usuario = {"nome": usuario.nome, "cpf": usuario.cpf, "telefone": usuario.telefone, "sexo": usuario.sexo,
                         "preco": usuario.preco_consulta, "nome_usuario": usuario.nome_usuario,
                         "senha_usuario": usuario.senha_usuario}
        return dados_usuario

    def abrir_tela(self):
        self.__tela_usuario.open()

    @property
    def tela_usuario(self):
        return self.__tela_usuario

    @property
    def usuario_logado(self):
        return self.__usuario_logado

    @usuario_logado.setter
    def usuario_logado(self, usuario_logado):
        self.__usuario_logado = usuario_logado
