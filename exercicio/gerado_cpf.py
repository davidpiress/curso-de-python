"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  3   1  5  4  5  4  5  3  4
   30  9 40  28 30 20 20 9  8

Somar todos os resultados: 
30+9+40+28+30+20+20+9+8 = 301
Multiplicar o resultado anterior por 10
194 * 10 = 1940
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 4
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 4
"""

nove_digitos = ''
for i in range(9):
    nove_digitos += str(random.randint(0,9))

contador_regressivo_1 = 10
lista = []
resultado_1 = 0
for digito in nove_digitos:
    resultado_1 =  int(digito) * contador_regressivo_1
    lista.append(resultado_1)
    contador_regressivo_1 -= 1

    multiplica_anterior = sum(lista) * 10


digito = multiplica_anterior % 11

digito = digito if digito <= 9 else 0

"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  3  1   5  4  5  4  5  3  4  4 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
"""

nove_digitos = nove_digitos + str(digito)

dez_digitos = nove_digitos[:10]
contador_regressivo_2 = 11
lista_2 = []
resultado_2 = 0
for ultimo_digito in dez_digitos:
    resultado_2 = int(ultimo_digito) * contador_regressivo_2

    lista_2.append(resultado_2)
    soma = sum(lista_2)

    resto = soma * 10
    segundo_digito = resto % 11

    contador_regressivo_2 -= 1

digito_2 = segundo_digito % 11

digito_2 = digito_2 if digito_2 <= 9 else 0

gerado_cpf = f'{dez_digitos}{digito_2}'

print(gerado_cpf)