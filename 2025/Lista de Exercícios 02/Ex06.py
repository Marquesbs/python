"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule
e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
8% para o INSS e 5% para o sindicato, faça um programa que nos dê o salário bruto, quanto pagou ao INSS,
quanto pagou ao sindicato e o salário líquido. Observe que Salário Bruto - Descontos = Salário Líquido. Calcule os
descontos e o salário líquido, conforme a tabela abaixo:
a. + Salário Bruto : R$
b. - IR (11%) : R$
c. - INSS (8%) : R$
d. - Sindicato ( 5%) : R$
e. = Salário Liquido : R$
"""
# Definindo as variáveis
ganho_por_hora = 0
horas_trabalhadas = 0
salario_bruto = 0
ir = 0
inss = 0
sindicato = 0
salario_liquido = 0

# Lendo os dados
ganho_por_hora = float(input("Digite quanto você ganha por hora: "))
horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))

# Calculando o salário bruto
salario_bruto = ganho_por_hora * horas_trabalhadas

# Calculando os descontos
ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05

# Calculando o salário líquido
salario_liquido = salario_bruto - (ir + inss + sindicato)

# Exibindo os resultados
print("Salário Bruto: R$", salario_bruto)
print("Desconto do IR (11%): R$", ir)
print("Desconto do INSS (8%): R$", inss)
print("Desconto do Sindicato (5%): R$", sindicato)
print("Salário Líquido: R$", salario_liquido)
