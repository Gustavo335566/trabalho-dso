from entidade.usuario import Usuario
from entidade.agenda import Agenda
from limite.tela_usuario import Tela_usuario
from controle.controlador_agenda import Controlador_Agenda
from controle.controlador_cliente import  ControladorClientes
from controle.controlador_consulta import ControladorConsulta
from limite.tela_usuario import Tela_usuario
class Controlador_usuario(Usuario, Agenda, Tela_usuario, Controlador_Agenda, ControladorClientes, ControladorConsulta):
    def __init__(self, controlador_principal):
        self.__usuarios = []
        self.__tela_usuario = Tela_usuario()
        self.__controlador_principal = ControladorPrincipal

    def cadastro_usuario(self):
        nome, nome_usuario, cpf, senha_usuario, sexo, telefone, tempo_consulta, preco_consulta = Tela_usuario.pega_dados_usuario()
        usuario = Usuario(nome, nome_usuario, cpf, senha_usuario, sexo, telefone, tempo_consulta, preco_consulta)
        self.__usuarios.append(usuario)
        mensagem = "cadastro realizado com sucesso"
        Tela_usuario.mostra_mensagem(mensagem)

    def finalizar(self):
        exit(0)
    def busca_usuario_nome_senha(self, nome_usuario, senha_usuario):
        for usuario in self.todos_usuarios:
            if(nome_usuario == usuario.nome_usuario and senha_usuario == usuario.senha_usuario):
                self.menu_usuario(usuario)

    @property
    def todos_usuarios(self):
        return self.__usuarios

    def exclui_meu_usuario(self, usuario: Usuario):
        palavra = Tela_usuario.palavra_chave()
        if palavra == "adm123":
            for i in self.__usuarios:
                if(usuario == i):
                    self.__usuarios.remove(i)
                    mensagem = "Usuario excluido com sucesso"
                    self.__tela_usuario.mostra_mensagem(mensagem)
                    break
            mensagem = "Usuario nao foi achado ou ja foi excluido"
            self.__tela_usuario.mostra_mensagem(mensagem)
        self.__tela_usuario.mostra_mensagem("Palavra chave incorreta")

    def menu_usuario(self, usuario: Usuario):
        switcher = {0: self.finalizar, 1: self.__controlador_principal.controlador_agenda.menu_agenda(usuario.agenda.minhas_consultas), 2: self.__controlador_principal.controlador_cliente.mostra_menu_clientes(),
                    3: self.__controlador_principal.controlador_consulta.mostra_menu_consulta(usuario.agenda.minhas_consultas), 4: self.consulta_feita, 5:self.alterar_dados_usuario,
                    6: self.cadastro_usuario(), 7: self.exclui_meu_usuario(usuario)}
        while True:
            opcao = Tela_usuario.tela_opcoes()
            funcao_escolhida = switcher[opcao]
            funcao_escolhida()

    def consulta_feita(self):
        consulta = self.__controlador_principal.controlador_cliente.pega_cliente_por_cpf(self.__tela_usuario.pega_cpf_cliente())
        if(consulta is str):
            mensagem = consulta
            self.__tela_usuario.mostra_mensagem(mensagem)
        else:
            #Tem que passar a consulta
            mensagem = self.__tela_usuario.mostra_mensagem(self.add_historico(consulta))
            self.__tela_usuario.mostra_mensagem(mensagem)

    def alterar_dados_usuario(self, usuario):
        switcher = {1: usuario.telefone(self.__tela_usuario.mudanca_telefone()), 2: usuario.preco_consulta(self.__tela_usuario.mudanca_preco()),
                    3: usuario.preco_consulta(self.__tela_usuario.tempo_consulta()), 4: usuario.nome(self.__tela_usuario.mudanca_nome()),
                    5: usuario.nome_usuario(self.__tela_usuario.mudanca_nome_usuario()), 6 : usuario.senha(self.__tela_usuario.mudanca_senha()),
                    7: usuario.sexo(self.__tela_usuario.mudanca_sexo()), 0: self.finalizar}
        while True:
            opcao = self.__tela_usuario.mudanca_dados_usuario()
            funcao_escolhida = switcher[opcao]
            funcao_escolhida()
