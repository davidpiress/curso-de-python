letra_colocada = ''
nome = 'davi'

while True:
    letra = input('Digite a letra: ')

    if len(letra) > 1:
        print('Você digitou mais de uma letra.')
        continue

    if letra in nome:
        letra_colocada += letra

    palavra_formada = ''
    for letra_do_nome in nome:
        if letra_do_nome in letra_colocada:
            palavra_formada += letra_do_nome
        else:
            palavra_formada += '*'

    print(palavra_formada)