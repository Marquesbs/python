def potencia(x):
    return x ** 2

numeros = [1, 2, 3, 4, 5]

# Usando a função map para aplicar a função potencia a cada elemento da lista numeros
resultado = list(map(potencia, numeros))

print(resultado)  # Saída: [1, 4, 9, 16, 25]
print("\n----------------------------------\n")
def fahrenheit(temp):
    return (temp * 9/5) + 32

def celsius(temp):
    return (temp - 32) * 5/9

temperaturas = [0, 22.5, 40, 100]

#Aplicando a função a cada elemento da lista temperaturas
#Em Python 3, a função map retorna um iterador, então precisamos converter para uma lista
map(fahrenheit, temperaturas)  # Converte Celsius para Fahrenheit

list(map(fahrenheit, temperaturas))

#Exibindo na tela os resultados
print(map(fahrenheit, temperaturas))
print(list(map(fahrenheit, temperaturas)))
print("\n----------------------------------\n")
#usaando loop para imprimir os resultados
for temp in map(fahrenheit, temperaturas):
    print(temp)
print("\n----------------------------------\n")

#Usando lambda para converter Celsius para Fahrenheit
#lambda é uma função anônima que pode ter qualquer número de argumentos, mas apenas uma expressão e executa essa expressão em tempo de execução.
map(lambda x: (5.0 / 9) * (x - 32), temperaturas)
