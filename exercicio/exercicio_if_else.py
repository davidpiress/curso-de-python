while True:
    primeiro_valor = input('Digite um valor: ')
    segundo_valor = input('Digite outro valor: ')

    try:
        primeiro_valor = int(primeiro_valor)
        segundo_valor  = int(segundo_valor)

        if primeiro_valor > segundo_valor:
            print(f'{primeiro_valor=} e maior que o {segundo_valor=}')
        elif segundo_valor > primeiro_valor:
            print(f'{segundo_valor=} e maior que o {primeiro_valor=}')
        else:
            print(f'{segundo_valor=} e {primeiro_valor=} são valores iguais')

    except ValueError:
        print('Digitação incorreta')