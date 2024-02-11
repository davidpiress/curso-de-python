"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        O seu nome é {nome}
        O seu nome invertido é {nome invertido}
        O seu nome contém (ou não) espaços
        O seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
    exiba "Desculpe, você deixou campos vazios."
"""

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

try:
    idade = int(idade)
    if nome and idade:
        print(f'Seu nome e {nome}')
        print(f'A sua idade e {idade}')
        print(f'Seu nome invertido e {nome[::-1]}')

        if ' ' in nome:
            print('contem espaços ')
        else:
            print('Não contem espaços')

        print(f'A quantidade  de letras e {len(nome)}')
        print(f'A primeira letra e {nome[0]}')
        print(f'A ultima letra e {nome[-1]}')
except ValueError:
    print("Desculpe, você deixou campos vazios.")
