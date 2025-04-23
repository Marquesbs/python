# Definindo operações
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b

print("\nBem-vindo à Calculadora!")

# Definindo função principal
def calculadora():
    print("\nSelecione a operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")

    while True:
        escolha = input("Digite sua escolha (1/2/3/4/5): ")
        
        if escolha not in ['1', '2', '3', '4', '5']:
            print("Opção inválida. Tente novamente.")
            continue

        match escolha:
            case '1':
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                print(f"{num1} + {num2} = {soma(num1, num2)}")
                break
            
            case '2':
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                print(f"{num1} - {num2} = {subtracao(num1, num2)}")
                break
            
            case '3':
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                print(f"{num1} * {num2} = {multiplicacao(num1, num2)}")
                break
            
            case '4':
                if num2 != 0:
                    num1 = float(input("Digite o primeiro número: "))
                    num2 = float(input("Digite o segundo número: "))
                    print(f"{num1} / {num2} = {divisao(num1, num2)}")
                else:
                    print("Erro: Divisão por zero não é permitida.")
                break
            
            case '5':
                print("Saindo da calculadora.")
                return False
        

calculadora()