def perguntar():
    resposta = input("O que deseja realizar? \n" +
                     "<I> - Para inserir um usuário\n" +
                     "<P> - Para Pesquisar um usuário\n" +
                     "<E> - Para excluir um usuário\n" +
                     "<L> - Para listar um usuário: ").upper()
    return resposta


def inserir(dicionario):
    dicionario[input("Digite o login: ").upper()] = [input("Digite o nome: ").upper(), input(
        "Digite a última data de acesso: ").upper(), input("Qual a última estação acessada: ").upper()]


def pesquisar(dicionario, chave):
    lista = dicionario.get(chave)
    if lista != None:
        print("Nome...........: " + lista[1])
        print("Último acesso..: " + lista[2])
        print("Última estação.: " + lista[3])


def excluir(dicionario, chave):
    if dicionario.get(chave) != None:
        del dicionario[chave]
    print("Objeto Eliminado")


def listar(dicionario):
    for chave, valor in dicionario.items():
        print("Objeto.....")
        print("Login: ", chave)
        print("Dados: ", valor)
