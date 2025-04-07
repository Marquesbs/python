lista = ["Maça", "Banana", "Laranja", "Uva"]

# Percorrendo a lista com while
i = 0
while i < 4:
    print(lista[i])
    i += 1
print("Fim do loop")

# Percorrendo a lista com while
i = 0
while i < len(lista):
    print(lista[i])
    i += 1
print("Fim do loop")

# Percorrendo a lista com for
for i in range(len(lista)):
    print(lista[i])
print("Fim do loop")

# Percorrendo a lista com for
for fruta in lista:
    print(fruta)
print("Fim do loop")