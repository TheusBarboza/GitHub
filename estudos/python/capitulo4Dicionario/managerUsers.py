usuarios = {}

opcao = input("Qual sua opção desejada?: \n"
              "<I> - Inserir dados do usuário\n"
              "<P> - Pesquisar dados do usuário\n"
              "<E> - Excluir usuário\n"
              "<L> - Listar usuários\n"
              "<S> - Sair\n"
              "\n"
              "Digite sua opção: ").upper()

while opcao == "I" or opcao == "P" or opcao == "E" or opcao == "L":
    if opcao == "I":
        chave = input("Digite o login: ").upper()
        usuarios[chave] = [input("Digite o nome: ").upper(), input(
            "Digite a última data de acesso: "), input("Qual a última estação acessada: ").upper()]

    opcao = input("Qual sua opção desejada?: \n"
                  "<I> - Inserir dados do usuário\n"
                  "<P> - Pesquisar dados do usuário\n"
                  "<E> - Excluir usuário\n"
                  "<L> - Listar usuários\n"
                  "<S> - Sair\n"
                  "\n"
                  "Digite sua opção: ").upper()
