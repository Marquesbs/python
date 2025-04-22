# O número 47 aparece nas duas listas?

lista1 = [10,16,24,39,47]
lista2 = [32,89,47,76,12]

# Loop externo
for elemento_lista1 in lista1:
    
    # Loop interno
    for elemento_lista2 in lista2:
        
        # Condicional
        if elemento_lista1 == 47 and elemento_lista2 == 47:
            
            print("O número 47 foi encontrado nas duas listas!")