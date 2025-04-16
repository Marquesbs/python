# Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar.

preco = float(input("Digite o preço da mercadoria: "))
desconto = float(input("Digite o percentual de desconto: "))

valorDesconto = preco * (desconto / 100)
valorAPagar = preco - valorDesconto

print(f"Valor do desconto: R$ {valorDesconto:.2f}")
print(f"Preço a pagar: R$ {valorAPagar:.2f}")