"""Crie uma lista com os números de 1 a 10 e use um for para imprimir cada número multiplicado por 2."""

# Criando uma lista com os números de 1 a 10
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Usando um loop for para imprimir cada número multiplicado por 2

for numero in numeros:
    resultado = numero * 2
    print(resultado)

# Alternativa com range
# Usando um loop for com range para imprimir cada número multiplicado por 2
for i in range(1, 11):
    resultado = i * 2
    print(resultado)
