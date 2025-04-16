"""
Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo
usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar,
sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.
"""

quantidadeKm = float(input("Digite a quantidade de Km percorrida: "))
quantidadeDias = int(input("Digite a quantidade de dias alugados: "))

precoPorDia = 60.00
precoPorKm = 0.15

precoTotal = (quantidadeDias * precoPorDia) + (quantidadeKm * precoPorKm)
print(f"O preço total a pagar é de R$ {precoTotal:.2f}")