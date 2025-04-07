lista = [0, 0, 0, 0, 0]

# Adicionando 5 elementos na lista
for i in range(5):
    lista[i] = int(input(f'Digite o {i + 1}º número: '))

# Exibindo os elementos da lista
print('Os números digitados foram:')
for i in range(5):
    print(lista[i], end=' ')
print()