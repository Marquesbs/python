arq = open('/home/bruno/Downloads/38-Cap06/arquivos/salarios.csv', 'r')

data = arq.read()

rows = data.split('\n')

print(rows)

full_data = []

for row in rows:
    split_row = row.split(',')
    full_data.append(split_row)
    first_row = full_data[0]

count = 0
for row in full_data:
    count += 1

print(f'Quantidade de linhas: {count}')
print(f'Quantidade de colunas: {len(full_data[0])}')

arq.close()