"""
    Essa condição e determinada que "in" ⇨ esta
    Essa outra condição e determinada que "not in" ⇨ não está, sera ao cotrario da condição
    Exemplo abaixo:
"""

nome = input('Digite seu nome: ')

if nome in 'vi':  # se (in)esta esse letras ao digitar no input
                  # sera verdeiro.
    print('Sim, tem dentro do nome as letras.')
else:
    print('Não tem dentro do nome as letras.')

nome = input('Digite seu nome: ')

if nome not in 'vi':  # se (not in)não está, essas letras "vi" ao digitar no input
                      # sera False porque a condição esta sendo ao contrario e
                      # com isso e else sera printado.
    print('Sim, tem dentro do nome as letras.')
else:
    print('else sendo executao por ser uma condição ao contrario')
    print('Não tem dentro do nome as letras.')
