

class TelaUsuario:
    def tela_opcoes(self):
        print("------USUARIO--------")
        print("1 - Agenda")
        print("2 - Cliente")
        print("3 - Consulta feita")
        print("4 - Alterar dados do usuario")
        print("5 - Ver dados usuario")
        print("6 - Excluir meu usuario")
        print("7 - Relatorio financeiro")
        print("8 - Historico do sistema")
        print("0 - Logout")
        lista = [1, 2, 3, 4, 5, 6, 7, 8, 0]
        while True:
            opcao = input("Escolha a opcao: ")
            if opcao.isdigit():
                if int(opcao) in lista:
                    return int(opcao)
            print("Valor incorreto")

    def pega_dados_usuario(self):
        nome_completo = str(input("Digite o seu nome: ")).capitalize()
        nome = nome_completo.replace(" ", "")
        while nome.isalpha() is False:
            print("O nome so pode conter letras")
            nome_completo = str(input("Digite o seu nome: "))
            nome = nome_completo.replace(" ", "")
        cpf = str(input("Digite o seu cpf: "))
        while cpf.isdigit() is False or len(cpf) != 11:
            print("CPF invalido")
            cpf = input("Digite o seu cpf: ")
        print("O nome de usuario pode conter somente letras e tem que ter de 8 a 20 caracteres, sem espacos.")
        nome_usuario = str(input("Digite o seu nome de usuario: "))
        while nome_usuario.isalpha() is False or len(nome_usuario) < 8 or len(nome_usuario) > 20:
            print("Somente letras e tamanho de nome do usuario de 8 a 20 caracteres")
            nome_usuario = str(input("Digite o nome do seu usuario: "))
        print("Senha letras e numeros, tamanho da senha de 8 a 16 algarismo")
        senha_usuario = str(input("Digite uma senha: "))
        while senha_usuario.isalnum() is False or senha_usuario.isdigit() is True\
                or senha_usuario.isalpha() or len(senha_usuario) < 8 or len(senha_usuario) > 16:
            print("Senha letras e numeros, tamanho da senha de 8 a 16 algarismo")
            senha_usuario = str(input("Digite uma senha: "))
        sexo = input("Digite o seu sexo [m/f]: ")
        while True:
            if sexo.upper() in "M" or sexo.upper() in "F":
                break
            print("Somente M ou F")
            sexo = input("Digite o seu sexo [m/f]: ")
        telefone = str(input("Digite o seu telefone no formato xx9xxxxxxxx: "))
        while telefone.isdigit() is False or len(telefone) != 11:
            print("Telefone invalido!")
            telefone = str(input("Digite o seu telefone no formato xx9xxxxxxxx: "))
        tempo_consulta = int(input("Tempo de consulta: "))
        while tempo_consulta > 60 or tempo_consulta < 10:
            print("Tempo de consulta somente em minutos, de 10min a 60min")
            tempo_consulta = int(input("Tempo de consulta: "))
        preco_consulta = float(input("Preco da consulta: "))
        while not preco_consulta > 0:
            print("Preco invalido!")
            preco_consulta = float(input("Preco da consulta: "))
        return nome, nome_usuario, cpf, senha_usuario, sexo, telefone, tempo_consulta, preco_consulta

    def mostra_mensagem(self, mensagem):
        print(mensagem)

    def mudanca_dados_usuario(self):
        print("Atencao digite apenas um dado de cada vez que voce queira alterar")
        print("1 - Telefone")
        print("2 - Preco da consulta")
        print("3 - Tempo da consulta")
        print("4 - Nome")
        print("5 - Nome de usuario")
        print("6 - Senha")
        print("7 - Sexo")
        print("0 - Sair")
        lista = [1, 2, 3, 4, 5, 6, 7, 0]
        while True:
            opcao = (input("Digite aqui o que voce quer mudar: "))
            if opcao.isdigit():
                if int(opcao) in lista:
                    return int(opcao)
            print("Valor incorreto")

    def pega_telefone(self):
        telefone = str(input("Digite o seu telefone no formato xx9xxxxxxxx: "))
        while telefone.isdigit() is False or len(telefone) != 11:
            print("Telefone inválido")
            telefone = str(input("Digite o seu telefone no formato xx9xxxxxxxx: "))
        return telefone

    def pega_tempo_consulta(self):
        tempo_consulta = int(input("Tempo de consulta: "))
        while 60 > tempo_consulta < 10:
            print("Tempo de consulta somente em minutos, de 10min a 60min")
            tempo_consulta = int(input("Tempo de consulta: "))
        return tempo_consulta

    def pega_senha_usuario(self):
        senha_usuario = str(input("Digite uma senha: "))
        while senha_usuario.isalnum() is False or senha_usuario.isdigit() is True or senha_usuario.isalpha() or len(
                senha_usuario) < 8 or len(senha_usuario) > 16:
            print("Senha deve ter letras e numeros, e ter de 8 a 16 caracteres")
            senha_usuario = str(input("digite uma senha: "))
        return senha_usuario

    def pega_nome(self):
        nome_completo = str(input("Digite o seu nome: ")).capitalize()
        nome = nome_completo.replace(" ", "")
        while nome.isalpha() is False:
            print("O nome so pode conter letras")
            nome_completo = str(input("Digite o seu nome: "))
            nome = nome_completo.replace(" ", "")
        return nome_completo

    def pega_nome_usuario(self):
        nome_usuario = str(input("Digite o seu nome de usuario: "))
        while nome_usuario.isalpha() is False or len(nome_usuario) < 8 or len(nome_usuario) > 20:
            print("O nome de usuario deve possuir somente letras e tamanho de 8 a 20 caracteres")
            nome_usuario = str(input("Digite o seu nome de usuario: "))
        return nome_usuario

    def pega_preco(self):
        preco_consulta = float(input("Preco da consulta: "))
        while not preco_consulta > 0:
            print("Preco invalido")
            preco_consulta = float(input("Preco da consulta: "))
        return preco_consulta

    def pega_cpf_usuario(self):
        cpf = str(input("Digite o seu cpf: "))
        while cpf.isdigit() is False or len(cpf) != 11:
            print("CPF inválido")
            cpf = input("Digite o seu cpf: ")
        return cpf

    def pega_sexo(self):
        sexo = str(input("Digite o seu sexo [m/f]: ")).upper()
        while sexo != "M" and sexo != "F":
            print("Somente M ou F")
            sexo = str(input("Digite o seu sexo [m/f]: ")).upper()
        return sexo

    def palavra_chave(self):
        palavra = str(input("Digite a palavra chave: "))
        return palavra

    def imprimir_dados_usuario(self, usuario):
        print(f"Nome:{usuario.nome} | Sexo:{usuario.sexo} | Telefone: {usuario.telefone} |"
              f"CPF:{usuario.cpf} | Preco Consulta: {usuario.preco_consulta}")
