name=input('Digite o nome do paciente: ')
age=int(input('Digite a idade do paciente: '))

if age>=65:
    print('O paciente',name,'POSSUI atendimento prioritário!')
else:
    print('O paciente',name,'NÃO possui atendimento prioritário!')
