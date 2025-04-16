'''
Dizemos que um número natural é triangular se ele é produto de três números naturais
consecutivos. Exemplo: 120 é triangular, pois 4.5.6 = 120. Dado um inteiro não-negativo n,
verificar se n é triangular.
'''

def e_triangular(n):
    for i in range(1, n):
        if i * (i + 1) * (i + 2) == n:
            print(f"{n} é triangular")
            break
        if i * (i + 1) * (i + 2) > n:
            print(f"{n} não é triangular")
            break

n = int(input("Digite um número inteiro não-negativo: "))

e_triangular(n)