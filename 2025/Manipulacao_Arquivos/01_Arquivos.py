arq = open('/home/bruno/Downloads/38-Cap06/arquivos/arquivo1.txt', 'r') # r = read

print(type(arq))

#lendo o arquivo
print(arq.read())

#contar quantas linhas tem o arquivo
print(arq.tell())

#resetando o cursor para o início do arquivo
print(arq.seek(0, 0))

#lendo os primeiros 23 caracteres
print(arq.read(23))

#lendo o arquivo
print(arq.read()) #lendo o restante do arquivo

print(arq.seek(0, 0))

arq.readlines() #lindo linha a linha

arq.close()