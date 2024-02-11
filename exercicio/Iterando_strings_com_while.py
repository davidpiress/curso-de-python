# Iterando strings com while
"""
nome = 'davi'   # para ser iterado no while
novo_nome = ''  # para jogar o nome na media que for iterado no while
indice = 0      # paraa iteração ser feita pelo while

while indice < len(nome): # o indice e 0 e vai com len que e a quantidade 
                          # de caracteres ate o indice final do nome
    
     letra = nome[indice] # vou jogar para a varivel letra p nome junto com indice
     
     novo_nome += letra   # agora tudo que joguue ppara varivel letra vou calcater 
                          # varivel de strng vazia
     
     indice += 1          # vai dar volta o hil ate a condição ser false no len(nome)

print(novo_nome)          # sera pritado quando laço while terminar com a volta no laço e ser false
"""


nome = 'marta'
indice = 0
nome_novo = ''

while indice < len(nome):
    letra = nome[indice]
    nome_novo += letra 

    indice += 1

print(nome_novo)






