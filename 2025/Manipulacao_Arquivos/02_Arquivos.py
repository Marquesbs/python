arq = open('/home/bruno/Downloads/38-Cap06/arquivos/arquivo2.txt', 'w') # w = write

print(arq.readable()) # False
print(arq.writable()) # True

arq.write('\nEssa é uma linha de texto\n') # sobreescreve o arquivo pois foi aberto como 'w'

arq.close()

arq = open('/home/bruno/Downloads/38-Cap06/arquivos/arquivo2.txt', 'a') # a = append

arq.write('\nEssa é uma nova linha de texto\n') # adiciona uma nova linha ao final do arquivo

arq.close()

arq = open('/home/bruno/Downloads/38-Cap06/arquivos/arquivo2.txt', 'r') # r = read

print(arq.read())

arq.close()