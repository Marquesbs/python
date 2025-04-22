"""
Escreva uma função que recebe um dado em texto.
Se esse dado tem mais de 20 caracteres, retorne que é um texto longo.
Se tem menos de 20 caracteres, retorne que é um texto pequeno.
"""

def classifica_texto(texto):
    """
    Classifica o texto como longo ou pequeno com base no número de caracteres.
    
    Args:
        texto (str): O texto a ser classificado.
    
    Returns:
        str: "Texto longo" se o texto tiver mais de 20 caracteres, 
             "Texto pequeno" caso contrário.
    """
    if len(texto) > 20:
        return "Texto longo"
    else:
        return "Texto pequeno"

# Testando a função
texto1 = "Esse é um texto longo com mais de 20 caracteres."
texto2 = "Pequeno."

print(classifica_texto(texto1))  # Deve retornar "Texto longo"
print(classifica_texto(texto2))  # Deve retornar "Texto pequeno"
