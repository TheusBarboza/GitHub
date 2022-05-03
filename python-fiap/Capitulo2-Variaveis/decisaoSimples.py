name=input('Digite o nome do paciente: ')
age=int(input('Digite a idade do paciente: '))
priority="NÃO"

if age>=65:
    priority="SIM"

print('O paciente',name,'possui atendimento prioritário?',priority)