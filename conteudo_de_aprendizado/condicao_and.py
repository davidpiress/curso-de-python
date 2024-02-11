# A condição 'and' so sera verdadeira caso
# as duas condições do if seja verdadeira,
# mas se uma das duas for false não sera
# executado a condição
numero = input('Digite um numero: ')
numero2 = input('Digite um numero: ')

try:
    numero = int(numero)
    numero2 = int(numero2)

    if numero == 4 and numero2 == 4:
        # A condição 'and' so sera verdadeira caso
        # as duas condições do if seja verdadeira.
        print('sao numeros iguais')
    else:
        print(f' foi digitado o {numero=} e {numero2=}')
except ValueError:
    print('não e um numero')
