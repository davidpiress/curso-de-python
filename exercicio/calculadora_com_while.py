"""
while True:

    try: 
        numero1 = input('digite um numero: ')
        numero2 = input('digite o outro numero: ')

        numero1 = int(numero1)
        numero2 = int(numero2)
    
        
    
        operador_de_calculo = input('digite o operador para o calculo: ')

        if operador_de_calculo == '+':
            print(numero1 + numero2)
        elif operador_de_calculo == '-':
            print(numero1 - numero2)
        elif operador_de_calculo == '*':
            print(numero1 * numero2)
        elif operador_de_calculo == '/':
            print(numero1 / numero2)
        else:
            print('operador incorreto')
    except ValueError:
        print('não e valido esse tipo de digitação')

    sair_ou_continuar = input('Digite sair ou continuar: ').lower()
    
    if sair_ou_continuar == 'sair':
        print('calculadorra fechada')
        break
    elif sair_ou_continuar == 'continuar':
        print('conculando novamente')
        continue
       
    else:
        print('não esta de acordo com as opçoẽs')

"""
while True:
    numero1 = input('digite um numero: ')
    numero2 = input('digite o outro numero: ')
    operador_de_calculo = input('Digite um operador (+-/*)')
        
    numero_digitado = None
        
    try:
        int_numero1 = int(numero1)
        int_numero2 = int(numero2)
        numero_digitado = True
    except:
        numero_digitado = None

        
    if numero_digitado is None:
        print('ambos numero são invalidos')
        continue

    operador = '+-/*'

    if operador_de_calculo not in operador:
        print('operador invalido')
        continue


    if len(operador_de_calculo) > 1:
        print('So pode digitar um operador.')
        continue
    

    if operador_de_calculo == '+':
        print(f'{int_numero1}+{int_numero2}= {int_numero1 + int_numero2}')
    elif operador_de_calculo == '-':
        print(f'{int_numero1}-{int_numero2}= {int_numero1 - int_numero2}')
    elif operador_de_calculo == '*':
        print(f'{int_numero1}*{int_numero2}= {int_numero1 * int_numero2}')
    elif operador_de_calculo == '/':
        print(f'{int_numero1}/{int_numero2}= {int_numero1 / int_numero2}')


    sair = input('deseja [c]ontinuar ou [s]air ?: ')

    if sair == 's':
        print('programa finalizado')
        break
    elif sair == 'c':
        print('programa reinicializado')
    else:
        print('Digitação invalida')
    
    sair = input('deseja [c]ontinuar ou [s]air ?: ')