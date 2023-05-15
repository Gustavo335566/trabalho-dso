from entidade.usuario import Usuario
from limite.telausuario import TelaUsuario


class ControladorUsuario:
    def __init__(self, controlador_principal):
        self.__usuarios = []
        self.__tela_usuario = TelaUsuario()
        self.__controlador_principal = controlador_principal

    def cadastro_usuario(self):
        nome, nome_usuario, cpf, senha_usuario, sexo, telefone, tempo_consulta,\
            preco_consulta = self.__tela_usuario.pega_dados_usuario()
        for i in self.__usuarios:
            while i.nome_usuario == nome_usuario:
                self.__tela_usuario.mostra_mensagem("nome de usuario ja usado, coloque outro")
                nome_usuario = self.__tela_usuario.pega_nome_usuario()
            while i.cpf == cpf:
                self.__tela_usuario.mostra_mensagem("CPF ja usado no usuario, voce ja possui usuario")
                cpf = self.__tela_usuario.pega_cpf_usuario()
        usuario = Usuario(nome, cpf, telefone, sexo, nome_usuario, senha_usuario, tempo_consulta, preco_consulta)
        self.__usuarios.append(usuario)
        mensagem = "cadastro realizado com sucesso"
        self.__tela_usuario.mostra_mensagem(mensagem)

    def busca_usuario_nome_senha(self, nome_usuario, senha_usuario):
        existe = False
        verificacao = False
        for usuario in self.todos_usuarios:
            if nome_usuario == usuario.nome_usuario and senha_usuario == usuario.senha_usuario:
                existe = True
                self.menu_usuario(usuario)
            elif nome_usuario == usuario.nome_usuario:
                verificacao = True
        if verificacao:
            self.__tela_usuario.mostra_mensagem("Usuario ou senha incorretos")
        if not existe:
            self.__tela_usuario.mostra_mensagem("Usuario nao cadastrado!")

    @property
    def todos_usuarios(self):
        return self.__usuarios

    def exclui_meu_usuario(self, usuario: Usuario):
        palavra = self.__tela_usuario.palavra_chave()
        if palavra == "adm123":
            for i in self.__usuarios:
                if usuario.cpf == i.cpf:
                    self.__usuarios.remove(i)
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

    def menu_usuario(self, usuario: Usuario):
        switcher = {1: self.__controlador_principal.controlador_agenda.menu_agenda,
                    2: self.__controlador_principal.controlador_cliente.mostra_menu_clientes,
                    3: self.consulta_feita,
                    4: self.alterar_dados_usuario,
                    5: self.exclui_meu_usuario,
                    6: self.calculo_financeiro,
                    7: self.historico_sistema,
                    0: 0}
        while True:
            opcao = self.__tela_usuario.tela_opcoes()
            funcao_escolhida = switcher[opcao]
            if opcao == 0:
                break
            elif opcao == 2 or opcao == 7:
                funcao_escolhida()
            else:
                if opcao == 5:
                    verificacao = funcao_escolhida(usuario)
                    if verificacao:
                        break
                else:
                    funcao_escolhida(usuario)

    def calculo_financeiro(self, usuario):
        calculo = len(usuario.relatorio) * usuario.preco_consulta
        self.__tela_usuario.mostra_mensagem(str(calculo))
        input()

    def consulta_feita(self, usuario):
        cliente = self.__controlador_principal.controlador_cliente.pega_cliente_por_cpf()
        if not isinstance(cliente, str):
            for data, horarios in usuario.agenda.minhas_consultas.items():
                for hora, consulta in horarios.items():
                    if consulta != "vago":
                        if consulta.cliente == cliente:
                            usuario.relatorio.append(consulta)
                            adicione_historico = self.__controlador_principal.controlador_cliente\
                                .adicionar_no_historico(consulta, usuario)
                            self.__controlador_principal.controlador_consulta.historico_consultas.append(adicione_historico)
        else:
            self.__tela_usuario.mostra_mensagem(cliente)
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

    def alterar_dados_usuario(self, usuario):
        switcher = {1: self.mudanca_telefone, 2: self.mudanca_preco, 3: self.mudanca_tempo_consulta,
                    4: self.mudanca_nome, 5: self.mudanca_nome_usuario, 6: self.mudanca_senha_usuario,
                    7: self.mudanca_sexo, 0: None}
        while True:
            opcao = self.__tela_usuario.mudanca_dados_usuario()
            funcao_escolhida = switcher[opcao]
            if opcao == 0:
                break
            else:
                funcao_escolhida(usuario)

    def imprimir_dados_usuario(self, usuario):
        for i in self.__usuarios:
            if i == usuario:
                self.__tela_usuario.imprimir_dados_usuario(usuario)
        input()
