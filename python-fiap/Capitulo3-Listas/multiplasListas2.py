equipamentos=[]
valores=[]
serial=[]
departamentos=[]
resposta='S'

while resposta=='S':
    equipamentos.append(input('Equipamento: '))
    valores.append(float(input('Valor: ')))
    serial.append(int(input('Número do Serial: ')))
    departamentos.append(input('Departamento: '))
    resposta=input('Digite \'S\' para continuar: ').upper()
for indice in range(0,len(equipamentos)):
    print('\nEquipamento..: ', (indice+1))
    print('Nome.........: ', equipamentos[indice])
    print('Valor........: ', valores[indice])
    print('Serial.......: ', serial[indice])
    print('Departamento.: ',departamentos[indice])