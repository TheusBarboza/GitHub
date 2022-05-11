resposta='SIM'
while resposta=='SIM':
    name=input('Digite o nome do paciente: ')
    age=int(input('Digite a idade do paciente: '))
    doenca_infectocontagiosa=input('Suspeita de doença infectocontagiosa? ').upper()
    while doenca_infectocontagiosa!='SIM' and doenca_infectocontagiosa!='NAO':
        print('Digite SIM ou NAO')
        doenca_infectocontagiosa = input('Suspeita de doença infectocontagiosa? ').upper()

    # PRIMEIRO PROBLEMA A SER RESOLVIDO
    if doenca_infectocontagiosa=="SIM":
        print('Encaminhe o paciente para sala AMARELA')
    else:
        print('Encaminhe o paciente para sala BRANCA')

    # SEGUNDO PROBLEMA A SER RESOLVIDO
    if age>=65:
        print('Paciente COM prioridade')
    else:
        gender=input('Digite o gênero do paciente: ').upper()
        if gender==('FEMININO') and age>10:
            pregnancy=input('A paciente está grávida? ').upper()
            if pregnancy=='SIM':
                print("Paciente COM prioridade")
            else:
                print('Paciente SEM prioridade')
        else:
            print('Paciente SEM prioridade')
        resposta=input('Digite SIM para continuar...').upper()