name=input('Digite o nome do paciente: ')
age=int(input('Digite a idade do paciente: '))
infectious_disease=input('Suspeita de doença infecto-contagiosa? ').upper()

if age>=65 and infectious_disease=="SIM":
    print('O paciente',name,'será direcionado para sala AMARELA = COM prioridade!')
elif age<65 and infectious_disease=="SIM":
    print('O paciente',name,'será direcionado para sala AMARELA = SEM prioridade!')
elif age>=65 and infectious_disease=="NAO":
    print('O paciente',name,'será direcionado para sala BRANCA = COM prioridade!')
elif age<65 and infectious_disease=="NAO":
    print('O paciente',name,'será direcionado para sala BRANCA = SEM prioridade!')
else:
    print('Responda a suspeita de doença infectocontagiosa com SIM ou NAO')
