# or - uma das condições tem que ser verdadeiro
# se  uma das duas condições for false

while True:
    entrar = input('Digite entrar: ')

    if entrar == 'entra' or entrar == 'ENTRA':
        # A condição 'and' so sera verdadeira caso
        # as duas condições do if seja verdadeira.
        print('Você entrou no programa')
    elif not entrar == 'entra' or entrar == 'ENTRA':
        print('digitação incorreta.')
        continue

    sair = input('Digite sair ou voltar: ')

    if sair == 'sair' or sair == 'SAIR':
        print(f' Vocẽ saiu do programa')
        break
    elif sair == 'voltar':
        continue
    else:
        print('digitação incorreta')

    sair = input('Digite sair ou voltar: ')
    if sair:
        continue

    entrar = input('Digite entrar: ')

    if entrar == 'entra' or entrar == 'ENTRA':
        print('Você entrou novamente no programa')
    else:
        print('digitação incorreta')

    sair = input('Digite sair ou voltar: ')

    if sair == 'sair' or sair == 'SAIR':
        print(f' Vocẽ saiu do programa')
        break
    elif sair == 'voltar':
        continue
