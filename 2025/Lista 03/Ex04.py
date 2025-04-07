"""
A  seqüência  de  Fibonacci  é  a  seguinte:  1,  1,  2,  3,  5,  8,  13,  21,  34,  55,  ...  Sua  regra  de 
formação é simples: os dois primeiros elementos são 1; a partir de então, cada elemento é a 
soma dos dois anteriores. Faça um algoritmo que leia um número inteiro calcule o seu número 
de Fibonacci. F1 = 1, F2 = 1, F3 = 2, etc.
"""

def fibonacci(n):
    if n <= 0:
        return 0
    
    elif n == 1:
        return 1
    
    else:
        a, b = 1, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b
    
# Solicita ao usuário um número inteiro
n = int(input("Digite um número inteiro: "))

# Calcula o número de Fibonacci correspondente
resultado = fibonacci(n)

# Exibe o resultado
print(f"O {n}º número de Fibonacci é: {resultado}")
