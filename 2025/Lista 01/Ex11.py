"""
Sabendo que str( ) converte valores numéricos para string, calcule quantos dígitos há em 2 elevado
a um milhão.
"""

calculo = 2 ** 1000000
resultado = str(calculo)
quantidadeDigitos = len(resultado)

print(f"A quantidade de dígitos em 2 elevado a um milhão é: {quantidadeDigitos}")