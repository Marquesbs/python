import re

#documentação: https://docs.python.org/3/library/re.html

musica = '''
Todos os dias quando acordo
Não tenho mais o tempo que passou
Mas tenho muito tempo
Temos todo o tempo do mundo
Todos os dias antes de dormir
Lembro e esqueço como foi o dia
Sempre em frente
Não temos tempo a perder
Nosso suor sagrado
É bem mais belo que esse sangue amargo
E tão sério
E selvagem
Selvagem
Selvagem
Veja o sol dessa manhã tão cinza
A tempestade que chega é da cor
Dos teus olhos castanhos
Então me abraça forte
Me diz mais uma vez
Que já estamos distantes de tudo
Temos nosso próprio tempo
Temos nosso próprio tempo
Temos nosso próprio tempo
Não tenho medo
Do escuro
Mas deixe
As luzes
Acesas
Agora
O que foi escondido
É o que se escondeu
E o que foi prometido
Ninguém prometeu
Nem foi tempo perdido
Somos tão jovens
Tão jovens
Tão jovens
'''

# Usando regex para contar as ocorrências de 'a'
ocorrencias_a = len(re.findall(r'a', musica, re.IGNORECASE))  
# o len() serve para contar quantos elementos existem na lista que re.findall() retorna.
# re.IGNORECASE torna a busca insensível a maiúsculas e minúsculas

print("A letra 'a' aparece", ocorrencias_a, "vezes.")

#Quantas vezes a palavra tempo aparece na música
ocorrencia_tempo = len(re.findall(r'tempo', musica, re.IGNORECASE))

print("A palavra 'tempo' aparece", ocorrencia_tempo, "vezes.")

#quantas palavras são seguidas de '!'
ocorrencia_excl = len(re.findall(r'\b\w+!', musica))
'''
\b garante que estamos capturando uma palavra completa (limite de palavra).
\w+ captura uma ou mais letras, números ou underscores (a palavra em si).
! verifica se a palavra é seguida pelo caractere de exclamação.
'''

print("A música contém", ocorrencia_excl,"palavras seguidas do símbolo de exclamação.")

regex4 = re.findall(r'(?<=\besse\s)\w+(?=\samargo\b)', musica)
'''
(?<=\besse\s) é um lookbehind que garante que a palavra antes da palavra que queremos contar seja "esse" (seguido de um espaço).

\w+ captura a palavra que está entre "esse" e "amargo".

(?=\samargo\b) é um lookahead que garante que a palavra seguinte seja "amargo", precedida de um espaço.
'''

print("Temos", len(regex4), "palavras com o antecessor 'esse' e sucessor 'amargo', são elas: ", regex4)

# Regex para capturar caracteres antes do acento
resultado = [re.match(r'^[a-zA-Z]*[áéíóúâêîôûãõ]+', palavra).group(0) for palavra in musica.split() if re.search(r'[áéíóúâêîôûãõ]', palavra)]
'''
r'^[a-zA-Z]*[áéíóúâêîôûãõ]+' captura a palavra até o primeiro caractere acentuado, incluindo o próprio caractere acentuado.

A função re.search(r'[áéíóúâêîôûãõ]', palavra) garante que a palavra contém pelo menos um caractere com acento.

re.match(...).group(0) extrai a parte da palavra até o primeiro caractere acentuado.
'''
print(resultado)
