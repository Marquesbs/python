#Criando uma função
def verifica_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

# Chamando a função e passando um número como parâmetro.
print(verifica_par(35))

print(verifica_par(10))

# Criando uma lista de números
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# A função filter() retorna um iterador que filtra os elementos de uma sequência (como uma lista, tupla ou string)
print(filter(verifica_par, lista))

print(list(filter(verifica_par, lista)))

# A função filter() pode ser usada com uma função lambda para simplificar o código
print(list(filter(lambda x: x % 2 == 0, lista)))

# A função filter() pode ser usada para filtrar elementos de uma lista com base em qualquer condição
# Exemplo: Filtrando números maiores que 8
print(list(filter(lambda num: num > 8, lista)))