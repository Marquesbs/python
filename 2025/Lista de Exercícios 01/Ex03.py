# Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos.

dias = int(input("Digite a quantidade de dias: "))
horas = int(input("Digite a quantidade de horas:"))
minutos = int(input("Digite a quantidade de minutos: "))
segundos = int(input("Digite a quantidade de segundos: "))

# Conversão de dias, horas e minutos para segundos
# 1 dia = 24 horas = 86400 segundos
# 1 hora = 60 minutos = 3600 segundos
# 1 minuto = 60 segundos

totalSegundos = (dias * 86400) + (horas * 3600) + (minutos * 60) + segundos
print(f"O total em segundos é: {totalSegundos}")
