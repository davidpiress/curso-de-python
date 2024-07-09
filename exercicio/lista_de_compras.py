#lista de compras 
#ter a possibilidade de usuario inserir
# Apagar
# Listar


lista = []
while True:
    print('Escolha um das opções para a lista de compra')
    opcao = input('[I]inserir, [a]pagar, [l]ista: ').lower()


    if opcao == 'i':
        adicionar_lista = input('Digite o produto para lista: ')
        lista.append(adicionar_lista)

    elif opcao == 'a':
        try:
            opcao_apagar = input('Escolha uns dos indices para apagar: ')
            indice = int(opcao_apagar)
            del lista[indice]
        except ValueError:
            print('Letras ou palavras não são validos')
        except Exception:
            print('Não existe lista para ser apagada.')

    elif opcao == 'l':
        for i, produto in enumerate(lista):
            print(i, produto)
    else:
        print('As oções so poder ser i, a e l.')