# Imprimindo um arquivo JSON copiado da Web
from urllib.request import urlopen
import json

# O arquivo JSON está em uma URL, então precisamos usar a função urlopen para abrir a URL
response = urlopen('https://vimeo.com/api/v2/video/57733101.json').read().decode('utf-8')
# O arquivo JSON é uma lista, então precisamos pegar o primeiro elemento
dados = json.loads(response)[0]

# Agora podemos acessar os dados do arquivo JSON
print('Título:', dados['title'])
print('URL:', dados['url'])
print('Duração:', dados['duration'])
print('Número de visualizações:', dados['stats_number_of_plays'])


arquivo_fonte = '/home/bruno/Downloads/38-Cap06/arquivos/dados.json'
arquivo_destino = '/home/bruno/Downloads/38-Cap06/arquivos/dados.txt'

# Copiando o arquivo JSON para um arquivo local
# Método 1
with open (arquivo_fonte, 'r') as infile:
    text = infile.read()
    with open (arquivo_destino, 'w') as outfile:
        outfile.write(text)

# Método 2
open (arquivo_destino, 'w').write(open(arquivo_fonte, 'r').read())
print("-----------------------")
# Leitura do arquivo copiado
with open(arquivo_destino, 'r') as arquivo:
    conteudo = arquivo.read()
    dados = json.loads(conteudo)
    print(conteudo)
    print("-----------------------")
    print(dados)
    # Se o arquivo for muito grande, podemos usar o método readlines() para ler linha por linha
    # for linha in arquivo:
    #     print(linha)