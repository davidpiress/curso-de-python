#split

frase = 'EU vou ate o FINAL, mais nunca desisto'
frase_split = frase.split(',')

lista = []

for i, frase in enumerate(frase_split):
    lista.append(frase_split[i].strip())
print(lista)

print()
print(frase_split)

#Join -unir as strings


frase1 = 'EU vou ate o FINAL, mais nunca desisto2'
frase_join = frase1.split(',')
lista2 = []

for i, palavra in enumerate(frase_join):
    lista2.append(frase_join[i])

frase_unida = '-'.join(lista2)
print(frase_unida)