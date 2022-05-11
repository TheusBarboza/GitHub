name=input('Digite o nome do paciente: ')
age=int(input('Digite a idade do paciente: '))
doenca_infectocontagiosa=input('Suspeita de doença infectocontagiosa? ').upper()

if age>=65:
    print('Paciente COM prioridade')
    if doenca_infectocontagiosa=="SIM":
        print('Encaminhe o paciente para sala AMARELA')
    elif doenca_infectocontagiosa=="NÃO":
        print('Encaminhe o paciente para sala BRANCA')
    else:
        print('Responda a suspeita de doença infectocontagiosa com SIM ou NAO')
else:
    print('Paciente SEM Prioridade')
    if doenca_infectocontagiosa=="SIM":
        print('Encaminhe o paciente para sala AMARELA')
    elif doenca_infectocontagiosa=="NAO":
        print('Encaminhe o paciente para sala BRANCA')
    else:
        print('Responda a suspeita de doença infectocontagiosa com SIM ou NAO')