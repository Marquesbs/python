"""
Dados dois números inteiros positivos, determinar o máximo divisor comum entre eles usando 
o algoritmo de Euclides. 
"""

def mdc(a, b):
    while b != 0:
        a, b = b, a % b
    return a


print("Cálculo do Máximo Divisor Comum (MDC) usando o Algoritmo de Euclides")
a = int(input("Digite o primeiro número inteiro positivo: "))
b = int(input("Digite o segundo número inteiro positivo: "))
    
if a <= 0 or b <= 0:
    print("Os números devem ser inteiros positivos.")
    
resultado = mdc(a, b)
print(f"O máximo divisor comum entre {a} e {b} é: {resultado}")