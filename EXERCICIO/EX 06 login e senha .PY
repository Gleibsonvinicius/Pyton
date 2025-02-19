import os

os.system("clear")


#Elabore um algoritmo para solicitar ao usuário o login e a senha.Considere que os dados do usuário já estão cadastrados.Caso o login e senha estejam corretos, mostre a mensagem: “Bem-vindo!” Caso contrário, mostre a mensagem: “Login ou senha inválidos.”



# Dados de login e senha já cadastrados
login_cadastrado = "usuario123"
senha_cadastrada = "senha123"

# Solicitar login e senha ao usuário
login = input("Digite o login: ")
senha = input("Digite a senha: ")

# Verificar se o login e senha estão corretos
if login == login_cadastrado and senha == senha_cadastrada:
    print("Bem-vindo!")
else:
    print("Login ou senha inválidos.")
