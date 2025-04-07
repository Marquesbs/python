lista = ["Bruno", "Ana", "Carlos", "Maria"]

# Copiando a lista
lista_copia = lista.copy()

# Adicionando um novo elemento na lista original
lista.append("João")
lista_copia[0] = "Pedro"

# Exibindo as duas listas
print("Lista original:", lista)
print("Lista cópia:", lista_copia)