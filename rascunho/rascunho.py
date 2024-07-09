# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]
qtd_acertou = 0
for pergunta in perguntas:
    print(f'Pergunta:{pergunta['Pergunta']}')
    print()

    opcoes = pergunta['Opções']
    for i, opcao in enumerate(opcoes):

        print(f'{i})', opcao)
    print()

    resposta = input('Escolha uma das opções: ')

    acertou = False
    int_resposta = None
    qtd_perguntas = len(opcoes)

    if resposta.isdigit():
        int_resposta = int(resposta)


    if int_resposta is not None:
        if int_resposta >= 0 and int_resposta < qtd_perguntas:
            if opcoes[int_resposta] == pergunta['Resposta']:
                acertou = True

    if acertou:
        qtd_acertou += 1
        print('acertou')
    else:
        print('errou')

print(f'Você acertou {qtd_acertou} de {qtd_perguntas}')