'''
Expressões regulares são padrões usados para combinar ou encontrar ocorrências de sequências de
caracteres em uma string. Em Python, expressões regulares são geralmente usadas para manipular strings
e realizar tarefas como validaçãod de entrada de dados, extração de informações de strings e substituição de texto.
'''
import re

texto = "Meu e-mail é exemplo@gmail.com e você pode me contatar em outro_email@yahoo.com."

# Expressão regular para contar quantas vezes o caracter arroba aparece no texto.
resultado = len(re.findall('@', texto))

print(f"O caracter '@' aparece {resultado} vezes no texto.")

# Expressão regular para extrair a palavra que aparece após a palavra 'você' em um texto.
resultado = re.findall(r'você (\w+)', texto) # o r antes da string representa a expressão regular em Python é usado para indicar que a string é uma string literal raw.
                                             # Isso significa que barras invertidas (\) dentro da string não são interpretadas como caracteres de escape, mas são incluídas na expressão regular como parte do padrão.

print(f"A palavra que aparece após 'você' é: {resultado[0]}") # o 0 entre colchetes faz com que o resultado seja exibido como uma lista, mas como só existe um resultado, o 0 indica que queremos o primeiro elemento da lista.

# Expressão regular para extrair endereços de e-mail de uma string.
emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', texto)

print(f"Os endereços de e-mail encontrados são: {emails}")

texto2 = "O aluno estava incrivelmente perdido, mas ele conseguiu encontrar a DSA e rapidamente começou a aprender."

# Extraindo advérbios da frase
for palavra in re.finditer(r'\b\w+mente\b', texto2):
    print('%02d-%02d: %s' % (palavra.start(), palavra.end(), palavra.group(0)))
