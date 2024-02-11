frase = 'aaaoooo.'

qtd_apareceu_mais_vzs = 0
letra_paraceu_m_vzs = ''

i = 0

while i < len(frase):
    letra = frase[i]

    if letra == ' ':
        i += 1
        continue

    qtd_letra_atual =  frase.count(letra)
    
    if qtd_apareceu_mais_vzs < qtd_letra_atual:
        qtd_apareceu_mais_vzs = qtd_letra_atual
        letra_pareceu_m_vzs = letra

    i += 1

print(f'a letra "{letra_pareceu_m_vzs}" apareceu {qtd_apareceu_mais_vzs} vezes')