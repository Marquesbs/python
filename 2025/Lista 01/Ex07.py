# Converta uma temperatura digitada em Celsius para Fahrenheit. F = 9*C/5 + 32

temperatura_Celsius = float(input("Digite a temperatura em Celsius: "))

temperatura_Fahrenheit = (9 * temperatura_Celsius) / 5 + 32

print(f"A temperatura em Fahrenheit é: {temperatura_Fahrenheit:.2f}°F")