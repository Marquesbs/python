#verificar a versão do python
from platform import python_version
print(f'Python version: {python_version()}')

'''
A função reduce() é uma função da biblioteca functools que aplica uma determinada função binária a pares
consecutivos de elementos em uma estrutura de dados iterável (como uma lista, tupla ou outro objeto iterável),
reduzindo a estrutura de dados a um único valor. A função binária é aplicada de forma cumulativa, ou seja,
o resultado da aplicação da função em um par de elementos é usado como entrada para a aplicação da função
aos próximos elementos.
A função reduce() é útil quando você deseja aplicar uma operação cumulativa a uma sequência de elementos,
como somar todos os elementos de uma lista, multiplicar todos os elementos de uma tupla ou aplicar
uma operação de agregação a uma coleção de dados.
A função reduce() é frequentemente usada em conjunto com funções lambda ou funções definidas pelo usuário.
A função reduce() é uma função de ordem superior, o que significa que ela pode receber outras funções como
argumentos. Ela é uma das funções mais poderosas e versáteis da biblioteca functools.
'''

# Importando a função reduce da biblioteca functools
from functools import reduce

#criando uma lista de números
lista = [47, 11, 42, 13]

print(f'Lista: {lista}')

def soma(a, b):
    soma = a + b
    return soma

#Usando reduce com uma função e uma lista.
print(reduce(soma, lista))

#usando reduce com uma função lambda e uma lista.
print(reduce (lambda x, y: x + y, lista))

# Podemos atribuir a função lambda a uma variável
# e usar essa variável como argumento da função reduce.
max_find = lambda a, b: a if (a > b) else b

print(type(max_find))

print(reduce(max_find, lista))