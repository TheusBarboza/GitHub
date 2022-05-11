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
for equipamento in equipamentos:
    print('Equipamento: ', equipamento)
