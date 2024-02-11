# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load
import os

# 'r' --> Usado somente pata ler o arquivo
# 'w' --> Usado somente pata escreve o arquivo
# 'r+' --> Usado somente pata escreve e ler o arquivo quando se usa o "seek"
# 'a' --> Usado para acrescentar algo no arquivo

caminho_do_txt = '/home/davi/PycharmProjects/curso-de-python/'
caminho_do_txt += 'Aula167.txt'

# arquivo = open(caminho_do_txt, 'r')
# arquivo.close()


"""# Abrindo, escrevendo e fechando o arquivo com "write"
with open(caminho_do_txt, 'w+') as arquivo:  # para que esse codigo abaixo seja executado sempre o "w+" tem que esta
    # presente para ser executado
    arquivo.write('linha1\n')
    arquivo.write('linha2\n')
    arquivo.writelines(('linha3\n', 'linha4\n'))  # Pode escrever em maisn de uma linha
    arquivo.seek(0, 0)      # Com o "seek" você pode jogar o curso de linha para cima e printa o que
    print(arquivo.read())   # esta nessa linha --> print(arquivo.read()), sem o "seek" você não consegue printar
    print('lendo')
    arquivo.seek(0, 0)
    print(arquivo.readline(), end='')
    print(arquivo.readline(), end='')
    print(arquivo.readline(), end='')
    print('REDLINES')
    arquivo.seek(0, 0)
    for linha in arquivo.readlines():
        print(linha.strip())

print('#' * 12)
# Lendo o arquivo com "read"
with open(caminho_do_txt, 'r') as arquivo:
    print(arquivo.read())

"""

with open(caminho_do_txt, 'w+') as arquivo:  # para que esse codigo abaixo seja executado sempre o "w+" tem que esta
    # presente para ser executado
    arquivo.write('atenção\n')
    arquivo.write('linha1\n')
    arquivo.write('linha2\n')
    arquivo.writelines(('linha3\n', 'linha4\n'))  # Pode escrever em maisn de uma linha
    arquivo.seek(0, 0)      # Com o "seek" você pode jogar o curso de linha para cima e printa o que
    print(arquivo.read())

# apaga um determinado arquivo com o import os
os.remove(caminho_do_txt)














