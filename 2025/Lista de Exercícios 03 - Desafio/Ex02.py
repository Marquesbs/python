"""
Indique como um troco deve ser dado utilizando-se um número mínimo de notas. Seu
algoritmo deve ler o valor da conta a ser paga e o valor do pagamento efetuado desprezando
os centavos. Suponha que as notas para troco sejam as de 50, 20, 10, 5, 2 e 1 reais, e que
nenhuma delas esteja em falta no caixa.
"""

# Definindo as notas disponíveis
notas = [50, 20, 10, 5, 2, 1]

def troco(n):
    # Calculando o troco
    troco = n[1] - n[0]
    print(f"Troco: {troco:.2f} reais")
    
    # Inicializando o dicionário para armazenar as notas
    troco_notas = {}
    
    # Calculando o número de notas para o troco
    for nota in notas:
        if troco >= nota:
            num_notas = troco // nota
            troco_notas[nota] = num_notas
            troco -= num_notas * nota
            
    return troco_notas

# Função principal
def main():
    # Lendo os valores da conta e do pagamento
    conta = float(input("Valor da conta: R$ "))
    pagamento = float(input("Valor do pagamento: R$ "))
    
    # Verificando se o pagamento é maior ou igual à conta
    if pagamento < conta:
        print("Pagamento insuficiente.")
        return
    
    # Chamando a função de troco
    resultado = troco([conta, pagamento])
    
    # Exibindo o resultado
    print("Notas para o troco:")
    for nota, quantidade in resultado.items():
        print(f"{quantidade:.0f} nota(s) de R$ {nota:.2f}")

if __name__ == "__main__":
    main()

