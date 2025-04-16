def saudacao(nome):
    return "Olá %s!" % nome

sds = saudacao("Bruno")

print(sds + " Tudo bem?")

def soma( a, b):
    return a + b

s = soma(5, 7)

print(s)

print(s + 5)

def profissao(nome):
    p = ""

    if nome == "Bruno":
        p = "Gestor de TI"
    else:
        p = "Não Identificado"
    
    return p

prof = profissao("Bruno")
print(prof)