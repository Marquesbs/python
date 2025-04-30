#importando um pacote Python
import numpy

#imprimindo todos os métodos e atributos do pacote
#dir() é uma função embutida do Python que retorna uma lista de atributos e métodos de um objeto
print(dir(numpy))

from numpy import sqrt #sqrt é um método do pacote numpy que calcula a raiz quadrada de um número

print(help(sqrt)) #help() é uma função embutida do Python que retorna a documentação de um objeto

import random #importando o pacote random

escolha = random.choice(['Abacate', 'Banana', 'Cenoura']) #escolhe um elemento aleatório de uma lista

print(escolha) #imprimindo o elemento escolhido aleatoriamente