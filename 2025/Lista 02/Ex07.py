"""
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a
ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida
em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem
compradas e o preço total. Obs. : somente são vendidos um número inteiro de latas.
"""

# Definindo as variáveis
area = 0
litros_por_lata = 18
preco_por_lata = 80.00
cobertura_por_litro = 3
latas = 0
preco_total = 0

# Lendo a área a ser pintada
area = float(input("Digite o tamanho em metros quadrados da área a ser pintada: "))

# Calculando a quantidade de litros necessários
litros_necessarios = area / cobertura_por_litro

# Calculando a quantidade de latas necessárias
latas = int(litros_necessarios / litros_por_lata) + (litros_necessarios % litros_por_lata > 0)

# Calculando o preço total
preco_total = latas * preco_por_lata

# Exibindo os resultados
print("Quantidade de latas de tinta a serem compradas:", latas)
print("Preço total: R$", preco_total)
