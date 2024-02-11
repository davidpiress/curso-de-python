"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.

- Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você vai conferir se a letra digitada está
na palavra secreta.
- Se a letra digitada estiver na palavra secreta; exiba a letra;
- Se a letra digitada não estiverna palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""


palavra_secreta = 'perfume'
letras_acertadas = ''
tentativas_de_acerto = 0
while True:
    letra = input('Digite a letra da palavra secreta :').lower()

    tentativas_de_acerto += 1


    if len(letra) > 1:
        print('so pode digitar uma letra.')
        continue


    palavra_formada = ''
    if letra in palavra_secreta:
        letras_acertadas += letra
    
    for letra_secreta in palavra_secreta:    # estou pegando a palavra_secreta e jogando para variavel
                                             # letra_secreta 
    
        if letra_secreta in letras_acertadas:# agorou quero saber se(if) letra_secreta esta(in) letras_acertadas
                                             # se esta nas letras_acertadas
            palavra_formada += letra_secreta # sera preintado letra 
        else:
            palavra_formada += '*'           # junto com o "*"



    print('->', palavra_formada)
    if palavra_formada ==  palavra_secreta:
        print('tentativas', tentativas_de_acerto)
        print('a palavra secreta e', palavra_formada)
        print('PARABENNNSS....')
        break
  