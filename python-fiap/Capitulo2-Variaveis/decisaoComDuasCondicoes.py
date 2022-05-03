name=input('Digite o nome do paciente: ')
age=int(input('Digite a idade do paciente: '))
infectious_disease=input('Suspeita de doença infecto-contagiosa? ').upper()

if age>=65:
    print('O paciente',name,'POSSUI atendimento prioritário!')
elif infectious_disease=="SIM":
    print('O paciente',name,'deve ser direcionado para sala de espera reservada.')
else:
    print('O paciente',name,'NÃO possui atendimento prioritário e pode aguardar na sala comum!')
