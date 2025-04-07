"""
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao 
nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
"""

# Solicita o nome de usuário
usuario = input("Digite o nome de usuário: ")

# Solicita a senha
senha = input("Digite a senha: ")

# Enquanto a senha for igual ao nome de usuário, solicita novamente
while senha == usuario:
    print("Erro: A senha não pode ser igual ao nome de usuário.")
    senha = input("Digite a senha novamente: ")

print("Cadastro realizado com sucesso!")