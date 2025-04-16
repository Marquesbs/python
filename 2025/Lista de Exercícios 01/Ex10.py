"""
Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a
quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante
perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o
total de dias.
"""

cigarrosPorDia = int(input("Digite a quantidade de cigarros fumados por dia: "))
anosFumando = int(input("Digite a quantidade de anos fumando: "))

minutosPerdidosPorCigarro = 10
diasPorAno = 365
minutosPorDia = 1440

minutosPerdidosPorDia = cigarrosPorDia * minutosPerdidosPorCigarro
diasPerdidos = (minutosPerdidosPorDia * diasPorAno * anosFumando) / minutosPorDia

print(f"Total de dias perdidos: {diasPerdidos:.2f}")