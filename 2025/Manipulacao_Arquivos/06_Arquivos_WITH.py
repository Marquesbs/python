# Manipulação de Arquivos com o comando with
# O comando with é utilizado para abrir arquivos de forma mais segura, pois ele garante que o arquivo será fechado corretamente, mesmo que ocorra um erro durante a leitura ou escrita.
with open('/home/bruno/Downloads/38-Cap06/arquivos/arquivo1.txt', 'r') as arquivo:
    conteudo = arquivo.read()

print(conteudo)