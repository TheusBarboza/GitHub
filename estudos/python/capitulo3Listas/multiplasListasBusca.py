equipamentos = []
valores = []
serial = []
departamentos = []
resposta = 'S'

while resposta == 'S':
    equipamentos.append(input('Equipamento: '))
    valores.append(float(input('Valor: ')))
    serial.append(int(input('Número do Serial: ')))
    departamentos.append(input('Departamento: '))
    resposta = input('Digite \'S\' para continuar: ').upper()

buscar = (input('Digite o nome do equipamento que deseja buscar: '))
for indice in range(0, len(equipamentos)):
    if buscar == equipamentos[indice]:
        print('Valor..: ', valores[indice])
        print('Serial.: ', serial[indice])
