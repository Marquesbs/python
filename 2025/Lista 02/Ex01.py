"""
Faça um Programa que peça os três lados de um triângulo. O programa deverá informar se os valores podem ser
um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
"""

def tipo_triangulo(lado1, lado2, lado3):
    if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
        return "Valores inválidos para os lados do triângulo."
    
    if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
        if lado1 == lado2 == lado3:
            return "Triângulo equilátero."
        elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
            return "Triângulo isósceles."
        else:
            return "Triângulo escaleno."
        
    else:
        return "Os valores não formam um triângulo."
    
lado1 = float(input("Digite o primeiro lado do triângulo: "))
lado2 = float(input("Digite o segundo lado do triângulo: "))
lado3 = float(input("Digite o terceiro lado do triângulo: "))
    
resultado = tipo_triangulo(lado1, lado2, lado3)
print(resultado)
