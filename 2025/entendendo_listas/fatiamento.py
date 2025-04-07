lista = ["Bruno", "Ana", "Carlos", "Maria", "João", "Pedro", "Lucas"]
lista_nova = lista[2:6]

print(lista_nova)
# Fatiamento da lista
nova_lista = lista[1:3]  
print(nova_lista)  

# Fatiamento com passo
nova_lista = lista[0:6:2]  
print(nova_lista) 

# Fatiamento com passo negativo
nova_lista = lista[::-1]  
print(nova_lista)  

# Fatiamento com passo negativo e intervalo
nova_lista = lista[3:0:-1]  
print(nova_lista)

