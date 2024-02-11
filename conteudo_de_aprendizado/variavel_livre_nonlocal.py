# Variavel livre + nonlocal

def fora(a):


    def dentro(): # a variavel livre e a aqui esta fora def dentro()
                  # aonde esta retornado p "a" mas se tivesse nomeado o
                  # "a" dentro do def dentro() não seria livre
        return a
    return dentro()

dentro = fora(10)
print(dentro)


















