from keyword import iskeyword


class TelaUsuario():
    def tela_opcoes(self):
        print("------USUARIO--------")
        print("1 - Agenda")
        print("2 - Cliente")
        print("3 - Consulta feita")
        print("4 - alterar dados do usuario")
        print("5 - cadastrar usuario")
        print("6 - excluir meu usuario")
        print("0 - deslogar")
        opcao = int(input("Escolha a opcao: "))
        lista = [1, 2, 3, 4, 5, 6, 0]
        while opcao not in lista:
            print("Valor incorreto")
            opcao = int(input("Escolha a opcao: "))
        return opcao

    def pega_dados_usuario(self):
        nome_completo = str(input("digite o seu nome: ")).capitalize()
        nome = nome_completo.replace(" ","")
        while nome.isalpha() is False:
            print("o nome so pode conter letras")
            nome_completo = str(input("digite o seu nome: "))
            nome = nome_completo.replace(" ", "")
        cpf = str(input("digite o seu cpf: "))
        while cpf.isalnum() is False and len(cpf) != 11:
            print("somente numeros ou atencao ao tamanho do cpf")
            cpf = input("digite o seu cpf: ")
        print("o nome de usuario pode conter somente letras e tem que ter de 8 a 20 caracteres, sem espacos.")
        nome_usuario = str(input("digite o seu nome de usuario: "))
        while nome_usuario.isalpha() is False or len(nome_usuario) < 8 or len(nome_usuario) > 20:
            print("Somente letras e tamanho de nome do usuario de 8 a 20 caracteres")
            nome_usuario = str(input("Digite o nome do seu usuario: "))
        print("Senha somente numeros, tamanho da senha de 8 a 16 algarismo")
        senha_usuario = str(input("digite uma senha: "))
        while senha_usuario.isalnum() is False or len(senha_usuario) < 8 or len(senha_usuario) > 16:
            print("Senha somente numeros, tamanho da senha de 8 a 16 algarismo")
            senha_usuario = str(input("digite uma senha: "))
        sexo = input("digite o seu sexo [m/f]: ")
        while True:
            if sexo.upper() in "M" or sexo.upper() in "F":
                break
            print("Somente m ou f")
            sexo = input("digite o seu sexo [m/f]: ")
        telefone = str(input("digite o seu telefone formato xx9xxxxxxxx: "))
        while telefone.isalnum() is False or len(telefone) != 11:
            print("Tamanho do numero invalido, somente DDD9xxxxyyyy")
            telefone = str(input("digite o seu telefone formato xx9xxxxxxxx: "))
        tempo_consulta = int(input("Tempo de consulta: "))
        while 60 > tempo_consulta < 10:
            print("Tempo de consulta somente em minutos, de 10min a 60min")
            tempo_consulta = int(input("Tempo de consulta: "))
        preco_consulta = float(input("Preco da consulta: "))
        while not preco_consulta > 0:
            print("preco invalido")
            preco_consulta = float(input("Preco da consulta: "))
        return nome, nome_usuario, cpf, senha_usuario, sexo, telefone, tempo_consulta, preco_consulta

    def mostra_mensagem(self, mensagem):
        print(mensagem)

    def mudanca_dados_usuario(self):
        print("Atencao digite apenas um dado de cada vez que voce queira alterar")
        print("1 - alterar o telefone")
        print("2 - alterar o preco da consulta")
        print("3 - tempo da consulta")
        print("4 - nome")
        print("5 - nome de usuario")
        print("6 - senha")
        print("7 - sexo")
        print("0 - para sair")
        opcao = int(input("Digite aqui o que voce quer mudar: "))
        lista = [1, 2, 3, 4, 5, 6, 7, 0]
        while opcao not in lista:
            print("Valor incorreto")
            opcao = int(input("Digite aqui o que voce quer mudar: "))
        return  opcao

    def pega_telefone(self):
        telefone = str(input("digite o seu telefone formato xx9xxxxxxxx: "))
        while telefone.isalnum() is False or len(telefone) != 11:
            print("Tamanho do numero invalido, somente DDD9xxxxyyyy")
            telefone = str(input("digite o seu telefone formato xx9xxxxxxxx: "))
        return telefone

    def pega_tempo_consulta(self):
        tempo_consulta = int(input("Tempo de consulta: "))
        while tempo_consulta.isalnum() is False or len(tempo_consulta) != 2:
            print("Tempo de consulta somente em minutos")
            tempo_consulta = int(input("Tempo de consulta: "))
        return tempo_consulta

    def pega_senha_usuario(self):
        senha_usuario = str(input("digite uma senha: "))
        while senha_usuario.isalnum() is False or len(senha_usuario) < 8 or len(senha_usuario) > 16:
            print("Senha somente numeros, tamanho da senha de 8 a 16 algarismo")
            senha_usuario = str(input("digite uma senha: "))
        return senha_usuario

    def pega_nome(self):
        nome_completo = str(input("digite o seu nome: ")).capitalize()
        nome = nome_completo.replace(" ", "")
        while nome.isalpha() is False:
            print("o nome so pode conter letras")
            nome_completo = str(input("digite o seu nome: "))
            nome = nome_completo.replace(" ", "")
        return nome_completo

    def pega_nome_usuario(self):
        nome_usuario = str(input("digite o seu nome de usuario: "))
        while nome_usuario.isalpha() is False or len(nome_usuario) < 8 or len(nome_usuario) > 20:
            print("Somente letras e tamanho de nome do usuario de 8 a 20 caracteres")
            nome_usuario = str(input("Digite o nome do seu usuario: "))
        return  nome_usuario

    def pega_preco(self):
        preco_consulta = float(input("Preco da consulta: "))
        while not preco_consulta > 0:
            print("preco invalido")
            preco_consulta = float(input("Preco da consulta: "))
        return  preco_consulta

    def pega_cfp_cliente(self):
        cpf = str(input("digite o seu cpf: "))
        while cpf.isalnum() is False and len(cpf) != 11:
            print("somente numeros ou atencao ao tamanho do cpf")
            cpf = input("digite o seu cpf: ")
        return cpf

    def pega_sexo(self):
        sexo = str(input("digite o seu sexo [m/f]: ")).upper()
        while sexo != "M" or sexo != "F":
            print("Somente m ou f")
            sexo = str(input("digite o seu sexo [m/f]: ")).upper()
        return sexo

    def palavra_chave(self):
        palavra = str(input("Digite a palavra chave: "))
        return palavra
