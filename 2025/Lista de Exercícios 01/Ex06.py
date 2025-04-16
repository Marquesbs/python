#Calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem.
# O tempo de viagem é calculado pela fórmula: tempo = distância / velocidade

distancia = float(input("Digite a distancia a percorrer (em Km): "))
velocidade = float(input("Digite a velocidade média esperada (em Km/h): "))

tempo = distancia / velocidade

print(f"Tempo estimado de viagem: {tempo:.2f} horas")