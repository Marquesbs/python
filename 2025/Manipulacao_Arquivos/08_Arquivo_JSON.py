# Criando um dicionário
dict_guido = {
    'nome' : 'Guido van Rossum',
    'linguagem' : 'Python',
    'similar' : ['c', 'Modula-3', 'lisp'],
    'users': 1000000
}

for k, v in dict_guido.items():
    print(k, v)

# Importando o módulo json
import json

json.dumps(dict_guido) # Converte o dicionário em uma string JSON

# Criando um arquivo JSON
with open('/home/bruno/Downloads/38-Cap06/arquivos/dados.json', 'w') as arquivo_json:

    arquivo_json.write(json.dumps(dict_guido, indent=4)) # Escreve o dicionário no arquivo JSON
    # indent=4 formata o JSON com 4 espaços de indentação

# Lendo o arquivo JSON
with open('/home/bruno/Downloads/38-Cap06/arquivos/dados.json', 'r') as arquivo_json:
    texto = arquivo_json.read() # Lê o arquivo JSON
    dados = json.loads(texto) # Converte o JSON em um dicionário
    
    print(dados['nome']) # Imprime o valor da chave 'nome'