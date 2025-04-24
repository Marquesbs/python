# Manipulando TXT
texto = "Essa é uma linha de texto\n"
texto = texto + "Essa é outra linha de texto\n"
texto += "Essa é a terceira linha de texto\n"

#importando o módulo os
import os

# Criando um arquivo
arquivo = open(os.path.join('/home/bruno/Downloads/38-Cap06/arquivos/arquivo_novo.txt'), 'w')

# Gravando o texto no arquivo
for palavra in texto.split():
    arquivo.write(palavra + ' ')

# Fechando o arquivo
arquivo.close()

arquivo = open('/home/bruno/Downloads/38-Cap06/arquivos/arquivo_novo.txt', 'r')
conteudo = arquivo.read()
print(conteudo)

arquivo.close()