# Criando lista de notas
notas = []

# Solicitando 5 notas ao usuario
for i in range(5):
    notas.append(float(input("Digite a nota: ")))

# Calculando a média
media = sum(notas) / len(notas) #sum() soma os elementos da lista e len() retorna o tamanho da lista

print(f"A média das notas é: {media:.2f}")



# Outra forma de fazer

# Criando lista de notas
notas = []

# Solicitando 5 notas ao usuario
for i in range(5):
    nota = float(input("Digite a nota: "))
    notas.append(nota)

# Calculando a média
i = 0
soma_notas = 0

while i < len(notas):
    soma_notas += notas[i]
    i += 1

media = soma_notas / len(notas) #len() retorna o tamanho da lista

# Exibindo a média
print(f"A média das notas é: {media:.2f}")