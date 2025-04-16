# Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário.

salarioAtual = float(input("Digite o valor do salário atual: "))
aumento = float(input("Digite a porcentagem do aumento: "))

# Cálculo do aumento
valorAumento = salarioAtual * (aumento / 100)
novoSalario = salarioAtual + valorAumento

print(f"O valor do aumento é: {valorAumento:.2f}")
print(f"O novo salário é: {novoSalario:.2f}")