"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
‘Loop’ infinito → Quando um código não tem fim
Continue → sempre vai pular uma determinada condição
Break → vaai para a condição e finalizar
"""
"""contador = 0

while True: 
    contador += 1


    if contador == 10:
        print('foi pulado o 10')
        continue

    if contador >= 20 and contador <= 30:
        print('pulou de novo')
        continue


    print(contador)

    if contador == 50:
        break
"""
"""
qtd_linhas = 5
qtd_colunas = 5

linhas = 1
while linhas <= qtd_linhas:
    colunas = 1
    while colunas <= qtd_colunas:
        print(f'{linhas} e {colunas}')
        colunas += 1
    linhas += 1
"""

"""contador = 0

while contador <= 10:
    contador += 1
    print(contador)"""

"""while contador <= 100:
    contador += 1

    if contador >= 50 and contador <= 60:
        print(f'foi excluida o {contador}')
        continue

    if contador == 99:
        print(f'foi excluida o {contador}')
        continue


    print(contador)"""


qtd_linhas = 5
qtd_colunas = 5

linha = 1

while linha <= qtd_linhas:
    coluna =  1
    while coluna <= qtd_colunas:
        print(f'{linha=}, {coluna=}')
        coluna += 1
    linha += 1