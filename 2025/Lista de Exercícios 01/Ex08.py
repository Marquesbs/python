# Converta uma temperatura digitada em Fahrenheit para Celsius. C = 5*(F-32)/9

temperatura_Fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))

temperatura_Celsius = 5 * (temperatura_Fahrenheit - 32) / 9

print(f"A temperatura em Celsius é: {temperatura_Celsius:.2f}°C")