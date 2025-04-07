#Criando lista de moveis
moveis = ["Sofá", "Mesa", "Cadeira", "Estante", "Cama", "Poltrona"]

i = 0
c = 0

# Verificando se o item está na lista
while i < 2:
    item_procurado = input("Digite o nome do item que você está procurando: ")
    while c < len(moveis):
        if moveis[c] == item_procurado:
            print(f"Item encontrado: {moveis[c]} no índice {c}")
            break
        if c == len(moveis)-1 and moveis[c] != item_procurado:
            print("Item não encontrado")
        c += 1
    i += 1
    c = 0

# Utilizando o for para verificar se o item está na lista
for item in moveis:
    item_procurado = input("Digite o nome do item que você está procurando: ")
    if item == item_procurado:
        print(f"Item encontrado: {moveis[c]} no índice {c}")
        break
    else:
        print("Item não encontrado")