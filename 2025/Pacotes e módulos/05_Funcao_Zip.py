#criando duas listas
x = [1, 2, 3]
y = [4, 5, 6]

# Unindo as listas. Em Python3, a função zip() retorna um iterador
print(zip(x, y))
print('\n')

# A função zip() retorna um iterador de tuplas, onde cada tupla contém um elemento de cada uma das listas
print(list(zip(x, y)))
print('\n')

# Atenção quando as sequências tiverem número diferente de elementos.
print(list(zip('ABCD', 'xy')))

#criando dois dicionários
d1 = {'a': 1, 'b': 2}
d2 = {'c': 4, 'd': 5}
print('\n')
print(list(zip(d1, d2.values())))

# Criando uma função que troca os valores entre dois dicionários
def troca_valores(d1, d2):
    dicTemp = {}

    for d1key, d2val in zip(d1, d2.values()):
        dicTemp[d1key] = d2val

    return dicTemp
print('\n')
print(troca_valores(d1, d2))