"""
Interpolação básica de strings
%s - strings
%d e i - int
%f ou %.2f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""

nome = 'davi'
idade = 30
preco_do_produto = 1000.57567
print('O %s, tem %d e com um produto de  R$%.2f' % (nome, idade, preco_do_produto))

print('O hexadecimal de %d e %020x' % (15, 15))
