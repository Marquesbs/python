"""
Supondo  que  a  população  de  um  país  A  seja  da  ordem  de  80000  habitantes  com  uma  taxa 
anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de 
crescimento de 1.5%. 

Faça um programa que calcule e escreva o número de anos necessários  para  que  a  população  do  país  A  ultrapasse  ou  iguale  a  população  do  país  B, 
mantidas as taxas de crescimento
"""

# Definindo as variáveis iniciais
populacao_a = 80000
populacao_b = 200000
crescimento_a = 0.03
crescimento_b = 0.015
anos = 0

# Loop para calcular o número de anos necessários
while populacao_a < populacao_b:
    populacao_a += populacao_a * crescimento_a
    populacao_b += populacao_b * crescimento_b
    anos += 1

# Exibindo o resultado
print(f"A população do país A ultrapassará a população do país B em {anos} anos.")