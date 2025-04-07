lista = []

print(type(lista))

numeros = [1, 2, 3, 4, 5]
print(type(numeros))
print(numeros)

nomes = ["Lucas", "Ana", "João"]
print(type(nomes))
print(nomes)

# Modificando elementos da lista
nomes[0] = "Maria"
print(nomes)

# Adicionando elementos a lista
numeros.append(6)
print(numeros)
nomes.append("Bruno")
print(nomes)

nome = nomes[3]
print(nome)

print("Meu nome é %s" % nomes[3])
