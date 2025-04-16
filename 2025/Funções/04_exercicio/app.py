"""
Crie uma função que retorna se um número é maior ou menor que 10.
O número deve ser passado como parâmetro
"""
#Criando função
def verifica(numero):
    if numero > 10:
        resultado = ("O número %d é maior que 10!" %numero)
    elif numero < 10:
        resultado = ("O número %d é menor que 10!" %numero)
    elif numero == 10:
        resultado = ("O numero %d é igual a 10!" %numero)
    else:
        resultado = ("O número não foi identificado.")
    return resultado

#Interação com o usuário fornecendo o número
num = int(input("Digite um numero: "))

#criando variável que chama a função retornando valores estabelecidos
result = verifica(num)

#exibe na tela o retorno
print(result)