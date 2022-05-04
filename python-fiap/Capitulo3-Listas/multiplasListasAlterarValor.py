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

depreciacao=input("\nDigite o nome do equipamento que será depreciado: ")
for indice in range(0,len(equipamentos)):
    if depreciacao==equipamentos[indice]:
        print("Valor antigo: ", valores[indice])
        valores[indice] = valores[indice] * 0.9
        print("Novo valor: ", valores[indice])