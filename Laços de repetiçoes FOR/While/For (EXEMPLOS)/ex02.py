
import os

os.system ("cls||clear")



login_correto = "usuario"
senha_correta = "senha123"


while True:
    login = input("Digite seu login: ")
    senha = input("Digite sua senha: ")
    
    if login == login_correto and senha == senha_correta:
        print("Login bem-sucedido!")
        break  
    else:
        print("Login ou senha incorretos. Tente novamente.")