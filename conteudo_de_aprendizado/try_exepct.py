"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""
while True:
    numero = input('Digite um numero: ')
    try:
        if numero.isdigit():
            numero = int(numero)
            print(f'O dobro do numero digitado e {numero * 2}')
            break
        else:
            print('numero não pode ser um float')
    except ValueError:
        print('Digitação incorreta por ser uma str')