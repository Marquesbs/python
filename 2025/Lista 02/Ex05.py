# Faça um Programa que leia três números e mostre o maior e o menor deles.

# Definindo as variáveis
num1 = 0
num2 = 0
num3 = 0
maior = 0

# Lendo os números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# Verificando o maior número
if num1 > num2 and num1 > num3:
    maior = num1

elif num2 > num1 and num2 > num3:
    maior = num2

elif num3 > num1 and num3 > num2:
    maior = num3

else:
    maior = num1

# Verificando o menor número
if num1 < num2 and num1 < num3:
    menor = num1

elif num2 < num1 and num2 < num3:
    menor = num2

elif num3 < num1 and num3 < num2:
    menor = num3

else:
    menor = num1

# Exibindo o resultado
print("O maior número é:", maior)
print("O menor número é:", menor)

