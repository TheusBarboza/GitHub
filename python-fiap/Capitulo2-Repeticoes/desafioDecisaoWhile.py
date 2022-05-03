resposta='SIM'
while resposta=="SIM":
    access=input('Qual o nível de acesso? (ADM, USR ou GUEST) :').upper()
    if access=='ADM' or access=='USR':
        gender=input('Qual o gênero da pessoa? (Feminino ou Masculino)').upper()
        if gender=="FEMININO" and access=='ADM':
            print('Olá Administradora!')
        elif gender=='FEMININO' and access=='USR':
            print('Olá Usuária!')
        else:
            if access=='ADM':
                print('Olá Administrador!')
            elif access=='USR':
                print('Olá Usuário')
    if access=='GUEST':
        print('Olá visitante!')
    else:
        print('Olá desconhecido(a)')
    resposta=input('Digite SIM para continuar: ').upper()