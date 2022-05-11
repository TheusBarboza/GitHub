def preencherInventario(lista):
    resp = 'S'
    while resp == 'S':
        equipamento = [input('Equipamento: '),
                       float(input('Valor: ')),
                       int(input('Número do Serial: ')),
                       input('Departamento: ')]
        lista.append(equipamento)
        resp = input('Digite \'S\' para continuar: ').upper()


def exibirInventario(lista):
    for elemento in lista:
        print('Nome.........: ', elemento[0])
        print('Valor........: ', elemento[1])
        print('Serial.......: ', elemento[2])
        print('Departamento.: ', elemento[3])


def localizarPorNome(lista):
    busca = input('\nDigite o nome do equipamento que deseja buscar: ')
    for elemento in lista:
        if busca == elemento[0]:
            print('Valor do equipamento: ', elemento[1])
            print('Serial do equipamento: ', elemento[2])


def depreciarPorNome(lista):
    depreciar = input(
        '\nDigite o nome do equipamento para depreciar seu valor: ')
    for elemento in lista:
        if depreciar == elemento[0]:
            print('Valor anterior do produto: ', elemento[1])
            elemento[1] = elemento[1] * ('1-porc/100')
            print('Valor após depreciação: ', elemento[1])


def excluirPorSerial(lista):
    excluir = input('\nDigite o serial do produto que deseja excluir: ')
    for elemento in lista:
        if excluir == elemento[2]:
            lista.remove(elemento)
    return 'Itens excluídos.'


def resumirValores(lista):
    valores = []
    for elemento in lista:
        valores.append(elemento[1])
    if len(valores) > 0:
        print('O equipamento mais caro custa: ', max(valores))
        print('O equipamento mais barato custa: ', min(valores))
        print('O total dos equipamentos é: ', sum(valores))
