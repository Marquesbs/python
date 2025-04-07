"""Escreva um programa que itere sobre uma string e conte quantas vogais (a, e, i, o, u) existem na string."""

# Definindo a string
string = "A programacao e uma habilidade essencial no mundo moderno."

# Inicializando o contador de vogais
contador_vogais = 0

# Definindo as vogais
vogais = "aeiouAEIOU"

# Iterando sobre cada caractere da string
for char in string:
    # Verificando se o caractere é uma vogal
    if char in vogais:
        # Incrementando o contador
        contador_vogais += 1

# Exibindo o resultado
print(f"A string contém {contador_vogais} vogais.")
