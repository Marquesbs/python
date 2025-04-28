import csv

with open('/home/bruno/Downloads/38-Cap06/arquivos/numeros.csv', 'w') as arquivo_csv:
    
    # Cria o objeto de gracação CSV
    escrever = csv.writer(arquivo_csv)

    # Grava no arquivo linha a linha
    escrever.writerow(('nota1', 'nota2', 'nota3'))
    escrever.writerow((10, 8, 9))
    escrever.writerow((7, 6, 5))
    escrever.writerow((8, 9, 10))

with open('/home/bruno/Downloads/38-Cap06/arquivos/numeros.csv', 'r', encoding = 'utf-8', newline = '\r\n') as arquivo:
    
    # Cria o objeto de leitura CSV
    leitor = csv.reader(arquivo)

    # Lê o arquivo linha a linha
    for linha in leitor:
        print(linha)
    
    # Lê o arquivo inteiro e armazena em uma lista
    dados = list(leitor)
    print(dados)

    #imprimir a partir da segunda linha
    for linha in dados[1:]:
        print(linha)