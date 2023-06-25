from entidade.usuario import Usuario
from limite.tela_usuario import TelaUsuario
from persistencia.usuario_dao import UsuarioDAO
from controle.controlador_agenda import ControladorAgenda


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
        for usuario in self.__usuario_dao.get_all():
            while usuario.nome_usuario == dados_usuario["nome_usuario"]:
                self.__tela_usuario.mostra_mensagem("nome de usuario ja usado, coloque outro")
                nome_usuario = self .__tela_usuario.pega_nome_usuario()
            while usuario.cpf == dados_usuario["cpf"]:
                self.__tela_usuario.mostra_mensagem("CPF ja usado no usuario, voce ja possui usuario")
                cpf = self.__tela_usuario.pega_cpf_usuario()
        usuario = Usuario(dados_usuario["nome"], dados_usuario["cpf"], dados_usuario["telefone"],
                          dados_usuario["sexo"], dados_usuario["nome_usuario"], dados_usuario["senha_usuario"],
                          dados_usuario["tempo_consulta"], dados_usuario["preco_consulta"], "Funcionario")
        agenda = self.__controlador_principal.controlador_agenda.criar_agenda_usuario(usuario.cpf, usuario.tempo_consulta)
        print(agenda)
        self.__usuario_dao.add(usuario.cpf, usuario)
        mensagem = "cadastro realizado com sucesso"
        self.__tela_usuario.mostra_mensagem("Aviso", mensagem)

    def busca_usuario_nome_senha(self, nome_usuario, senha_usuario):
        existe = False
        verificacao = False
        for usuario in self.__usuario_dao.get_all():
            if nome_usuario == usuario.nome_usuario and senha_usuario == usuario.senha_usuario:
                existe = True
                self.menu_usuario(usuario)
            elif nome_usuario == usuario.nome_usuario:
                verificacao = True
        if verificacao:
            self.__tela_usuario.mostra_mensagem("Usuario ou senha incorretos")
        if not existe:
            self.__tela_usuario.mostra_mensagem("Usuario nao cadastrado!")

    def exclui_meu_usuario(self, usuario: Usuario):
        palavra = self.__tela_usuario.palavra_chave()
        if palavra == "adm123":
            for i in self.__usuario_dao.get_all():
                if usuario.cpf == i.cpf:
                    self.__usuario_dao.remove(i)
                    mensagem = "Usuario excluido com sucesso"
                    self.__tela_usuario.mostra_mensagem(mensagem)
                    return True
            mensagem = "Usuario nao foi achado ou ja foi excluido"
            self.__tela_usuario.mostra_mensagem(mensagem)
            return False
        self.__tela_usuario.mostra_mensagem("Palavra chave incorreta")
        return False

    def historico_sistema(self):
        historico = self.__controlador_principal.controlador_consulta.historico_consultas
        for i in historico:
            self.__tela_usuario.mostra_mensagem(i)
        input()

    def calculo_financeiro(self):
        calculo = len(self.__usuario_logado.relatorio) * self.__usuario_logado.preco_consulta
        self.__tela_usuario.mostra_mensagem("Relatorio Financeiro", f"Total ganho: R${calculo:.2f}")

    def consulta_feita(self, usuario):
        if self.se_tem_consultas(usuario):
            cliente = self.__controlador_principal.controlador_cliente.pega_cliente_por_cpf()
            codigo_consulta_escolhida = self.__controlador_principal.controlador_consulta.pega_codigo_por_cliente(cliente)
            if not isinstance(cliente, str):
                for data, horarios in usuario.agenda.minhas_consultas.items():
                    for hora, consulta in horarios.items():
                        if consulta != "vago":
                            if consulta.cliente == cliente:
                                if codigo_consulta_escolhida == consulta.codigo:
                                    usuario.relatorio.append(consulta)
                                    adicione_historico = self.__controlador_principal.controlador_cliente\
                                        .adicionar_no_historico(consulta, usuario)
                                    self.__controlador_principal.controlador_consulta.historico_consultas.append(adicione_historico)
            else:
                self.__tela_usuario.mostra_mensagem(cliente)
        else:
            self.__tela_usuario.mostra_mensagem('não há consultas')
        input()

    def mudanca_telefone(self, usuario):
        telefone = self.__tela_usuario.pega_telefone()
        usuario.atualiza_atributo("telefone", telefone)

    def mudanca_preco(self, usuario):
        preco_consulta = self.__tela_usuario.pega_preco()
        usuario.atualiza_atributo("preco_consulta", preco_consulta)

    def mudanca_tempo_consulta(self, usuario):
        tempo_consulta = self.__tela_usuario.pega_tempo_consulta()
        usuario.atualiza_atributo("tempo_consulta", tempo_consulta)

    def mudanca_nome(self, usuario):
        nome = self.__tela_usuario.pega_nome()
        usuario.atualiza_atributo("nome", nome)

    def mudanca_nome_usuario(self, usuario):
        nome_usuario = self.__tela_usuario.pega_nome_usuario()
        usuario.atualiza_atributo("nome_usuario", nome_usuario)

    def mudanca_senha_usuario(self, usuario):
        senha_usuario = self.__tela_usuario.pega_senha_usuario()
        usuario.atualiza_atributo("senha_usuario", senha_usuario)

    def mudanca_sexo(self, usuario):
        sexo = self.__tela_usuario.pega_sexo()
        usuario.atualiza_atributo("sexo", sexo)

    def pega_dados_usuario(self):
        usuario = self.__usuario_logado
        dados_usuario = {"nome": usuario.nome, "cpf": usuario.cpf,"telefone": usuario.telefone, "sexo": usuario.sexo,
                         "preco": usuario.preco_consulta}
        return dados_usuario


    def se_tem_consultas(self, usuario):
        cont = False
        for k, v in usuario.agenda.minhas_consultas.items():
            for hora, disponibilidade in v.items():
                if disponibilidade != 'vago':
                    cont = True
        if cont:
            return cont
        else:
            return None

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
