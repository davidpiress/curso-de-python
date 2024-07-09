"""
operação ternaria (condicional de uma linha)
<valor ser verdadeiro if <condição> else <outro valor ser false>
"""
numero = input('Digite um numero: ')
numero = int(numero)
lista_numeros = [1, 2, 3, 4, 5]
lista = lista_numeros

if_ternario = "tem esse valor" if numero in lista  else 'não existe esse valor'
print(if_ternario)


if numero in lista:
    print('tem esse numero')
else:
    print('não tem esse numero')