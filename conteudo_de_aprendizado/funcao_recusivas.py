# Funções recursivas e recursividade
# - funções que podem se chamar de volta
# - úteis p/ dividir problemas grandes em partes menores
# Toda função recursiva deve ter:
# - Um problema que possa ser dividido em partes menores
# - Um caso recursivo que resolve o pequeno problema
# - Um caso base que para a recursão
# - fatorial - n! = 5! = 5 * 4 * 3 * 2 * 1 = 120
# https://brasilescola.uol.com.br/matematica/fatorial.htm

def recusiva(inicio=0, fim=10):  # Inicio e fim com algumentos nomeados
    if fim >= 10:                # aqui existe comdição com um limitador, porque se não existir o proprio python
        return fim               # para e execução da função e sera True de acordo com o função

    inicio += 1                  # A cada vonta na função sera sera soma mais um
    return recusiva(inicio, fim) # E o retorno do inicio e fim que sera retornado

print(recusiva())

# - fatorial - n! = 5! = 5 * 4 * 3 * 2 * 1 = 120
# Exemplo:

def factorial(n):                # função vai de traz pra frente 5, 4, 3, 2, 1
    if n <= 1:                   # so entra no if quando a condição puder retornar 1
        return 1

    return n * factorial(n - 1)  # Quando chega nessa parte multiplica a cada volta na função

print(factorial(5))              # E aonde o valor e reconehcido pela função


