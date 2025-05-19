import os

os.system ("cls||clear")



login_correto = "usuario"
senha_correta = "senha123"


tentativas_maximas = 3


for tentativa in range(tentativas_maximas):
  
    login = input("Digite seu login: ")
    senha = input("Digite sua senha: ")
    
   
    if login == login_correto and senha == senha_correta:
        print("Login bem-sucedido!")
        break  
    else:
        print("Login ou senha incorretos. Tente novamente.")
        

if tentativa == tentativas_maximas - 1:
    print("Número máximo de tentativas atingido. Programa encerrado.")