"""
Crie uma função que exibe a multiplicação de dois números
Os números devem ser passados por parâmetro
"""
#criando a funcao
def multiplica(n1, n2):
    resultado = n1 * n2
    print(f"\nO resultado da multiplicação de {n1} por {n2} é de {resultado}!")

print("\nMultiplicador de numeros\n")

#definindo variáveis
primeiroNumero = int(input("Digite o primeiro número: "))
segundoNumero = int(input("Digite o segundo número: "))

#chamando função
multiplica(primeiroNumero, segundoNumero)