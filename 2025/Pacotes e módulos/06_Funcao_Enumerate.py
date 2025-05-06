'''
A função enumerate() é uma função que permite iterar sobre uma estrutura de dados (como uma lista ou uma tupla).
A função retorna um objeto enumerado, que pode ser usado em loops para percorrer a estrutura de dados e acessar o contador e o valor de cada elemento.
'''

# Criando uma lista
lista = ['a', 'b', 'c', 'd', 'e']

# Usando a função enumerate() para iterar sobre a lista
print(enumerate(lista))
print('\n----------------\n')
# Convertendo o objeto enumerado em uma lista para visualizar os resultados
print(list(enumerate(lista)))
print('\n----------------\n')
# Imprimindo os valores de uma lista com a função enumerate() e seus respectivos indices.
for indice, valor in enumerate(lista):
    print(f'Índice: {indice}, Valor: {valor}')

print('\n----------------\n')

# Imprimindo os valores de uma lista com a função enumerate() e seus respectivos indices, mas limitando a impressão a 2 elementos.
for indice, valor in enumerate(lista):
    if indice >= 2:
        break
    else:
        print(valor)

print('\n----------------\n')

lista = ['Marketing', 'Vendas', 'Financeiro', 'RH', 'TI']

for indice, item in enumerate(lista):
    print(f'Índice: {indice}, Valor: {item}')
print('\n----------------\n')

for i, item in enumerate('Data Science Academy'):
    print(f'Índice: {i}, Valor: {item}')
print('\n----------------\n')

for i, item in enumerate(range(10)):
    print(f'Índice: {i}, Valor: {item}')
print('\n----------------\n')